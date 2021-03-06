import glob
import operator
import os
import time

from DisassemblyMnemonicNgramGenerator import DisassemblyMnemonicNgramGenerator

MAX_DISTANCE = 1

MAX_DISTANCE_FROM_PROTOTYPE = .01
MAX_CLUSTER_DISTANCE = .15

import logging

# Set logging for this module
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)


class ClusterNode(object):

    def __init__(self, disass_mnemonic_ngram_gen, cluster_id=None, nearest_prototype_cluster_node=None):
        assert isinstance(disass_mnemonic_ngram_gen, DisassemblyMnemonicNgramGenerator), \
            "Expected an object of type DisassemblyMnemonicNgramGenerator"

        self._disass_mnemonic_ngram_gen = disass_mnemonic_ngram_gen

        self._assigned_cluster = None

        # prototype node this node is associated with;
        self._nearest_prototype_cluster_node = nearest_prototype_cluster_node

    @staticmethod
    def distance(node_a, node_b):
        return 1 - ClusterNode.similarity(node_a, node_b)

    @staticmethod
    def similarity(node_a, node_b):
        import numpy as np
        """
        Compute the jaccard similarity of the hashed_ngram_sets of Node A and Node B

        :param node_a: Node A
        :param node_b: Node B
        :return:
        """

        assert isinstance(node_a, ClusterNode), "Expected cluster node object"
        assert isinstance(node_b, ClusterNode), "Expected cluster node object"

        jaccard_similarity = 0
        a_set=np.array(list(node_a._disass_mnemonic_ngram_gen.hashed_ngram_set))
        b_set=np.array(list(node_b._disass_mnemonic_ngram_gen.hashed_ngram_set))
        intersection = len(list(set(a_set).intersection(b_set)))
        union = (len(a_set) + len(b_set)) - intersection
        jaccard_similarity=float(intersection) / union
                
        # logger.warning("@todo: Need to implement jaccard similarity")

        """
        Hint: Suppose we have two sets, Set A and Set B, the Jaccard similarity is expressed as the number of 
              intersecting elements of the two sets diveded by the number of elements in the union of those sets 
              In this context, the sets are the 'hashed_n_gram_set' property for each respective ClusterNode object
        """

        return jaccard_similarity

    @property
    def assigned_cluster(self):
        """
         Cluster that this node belongs to
        :return:
        """
        return self._assigned_cluster

    @assigned_cluster.setter
    def assigned_cluster(self, value):
        self._assigned_cluster = value

    @property
    def cluster_id(self):
        if self._assigned_cluster is None:
            return None

        return self._assigned_cluster.cluster_id

    @property
    def is_prototype(self):
        return self == self._nearest_prototype_cluster_node

    @property
    def hashed_n_gram_set(self):
        return self._disass_mnemonic_ngram_gen.hashed_ngram_set

    @property
    def name(self):
        return self._disass_mnemonic_ngram_gen.binary_name

    @property
    def binary_sha256_hash(self):
        return self._disass_mnemonic_ngram_gen.binary_sha256_hash

    @property
    def nearest_prototype_cluster_node(self):
        return self._nearest_prototype_cluster_node

    @nearest_prototype_cluster_node.setter
    def nearest_prototype_cluster_node(self, value):
        self._nearest_prototype_cluster_node = value


class Cluster(object):

    def __init__(self, cluster_node_list=[]):

        self._cluster_id = id(self)

        self._cluster_node_list = []

        for cluster_node in cluster_node_list:
            self.add_node_to_cluster(cluster_node)

    def add_node_to_cluster(self, cluster_node):

        # Update node's cluster assignment
        cluster_node.assigned_cluster = self

        # Add node to cluster's node list
        self._cluster_node_list.append(cluster_node)

    def merge_cluster(self, cluster_2_merge):

        for cluster_2_merge_node in cluster_2_merge.cluster_nodes:
            self.add_node_to_cluster(cluster_2_merge_node)

    @property
    def cluster_nodes(self):

        for cluster_node in self._cluster_node_list:
            yield cluster_node

    @property
    def cluster_node_list(self):
        return self._cluster_node_list

    @staticmethod
    def complete_linkage_distance(cluster_a, cluster_b):

        """
         Computes the complete linkage distance of two clusters
        :param cluster_a:
        :param cluster_b:
        :return:
        """

        # Note: Complete linkage computes the maximum distance of a pair of nodes from cluster a
        #       and cluster b

        max_distance = 0

        for cluster_a_node in cluster_a.cluster_nodes:

            for cluster_b_node in cluster_b.cluster_nodes:

                distance = ClusterNode.distance(cluster_a_node, cluster_b_node)

                # If the distance between the current pair of notes is greater than max distance,
                # the current distance is the new max distance
                if distance > max_distance:
                    max_distance = distance

        return max_distance

    @property
    def cluster_id(self):
        return self._cluster_id


class ApproxAgglomerativeClustering(object):

    def __init__(self, max_cluster_distance=MAX_CLUSTER_DISTANCE ,data_set=None):

        self._data_set = data_set

        self._cluster_node_list = []

        self._cluster_list = []

        self._max_cluster_distance = max_cluster_distance

    def load_binaries_from_directory(self, binary_directory_path):


        for binary_file_path in glob.glob(os.path.join(binary_directory_path, '*.pb.z')):

            cur_iteration_start_time = time.time()

            binary_base_name = os.path.basename(binary_file_path)

            disass_mnemonic_ngram_gen = DisassemblyMnemonicNgramGenerator.from_disassembly_file(binary_file_path)

            self._cluster_node_list.append(ClusterNode(disass_mnemonic_ngram_gen))

            # logger.info("\nLoading the  disassembly proto for binary '{}'".format(binary_base_name))


        return self._cluster_node_list

    def perform_clustering(self):

        # Step 1: Determine the prototypes
        prototype_list = self._get_prototypes()

        # Step 2: Cluster Prototypes
        self._cluster_list = self.cluster_nodes(prototype_list)

        counter = 0

        number_nodes = len(self._cluster_node_list)

        # Step 3: Propagate Cluster assignments to nearest prototype
        for cluster_node in self._cluster_node_list:

            counter +=1

            if cluster_node.is_prototype:
                continue

            # Get cluster assignment from nearest prototype
            nearest_prototype_assigned_cluster = cluster_node.nearest_prototype_cluster_node.assigned_cluster

            # Add cluster node to cluster
            nearest_prototype_assigned_cluster.add_node_to_cluster(cluster_node)

            if counter%10 ==0:
                return

                # print("\n[ {}/{} ] Cluster node {} assigned to cluster {}".format(counter,number_nodes,
                #                                                               repr(cluster_node.name),
                #                                                         nearest_prototype_assigned_cluster.cluster_id))
                

                
    def cluster_nodes(self, cluster_node_list):
        # Note: Initially, every cluster node is its own cluster in agglomerative hierarchical clustering
        cluster_list = [Cluster([cluster_node]) for cluster_node in cluster_node_list]

        while True:

            # print("\n**** Current number of clusters: {}*****".format(len(cluster_list)))

            # Step 1: Compute distances of the clusters
            cluster_distance_dict = self._compute_cluster_distances(cluster_list)

            # Step 2:  Get the minimum cluster distances

            (min_cluster_pair, min_cluster_distance_value) = self.get_min_cluster_distance(cluster_distance_dict)

            if len(min_cluster_pair) <2:
                break


            # # print(
            # #     "Minimum Distance of {} is between current cluster {} and cluster {}".format(min_cluster_distance_value,
            # #                                                                                  min_cluster_pair[
            #                                                                                      0].cluster_id,
            #                                                                                  min_cluster_pair[
            #                                                                                      1].cluster_id))

            if min_cluster_distance_value >= self._max_cluster_distance:
                break


            # Step 3: Merge the min pair clusters
            min_cluster_a = min_cluster_pair[0]
            min_cluster_b = min_cluster_pair[1]

            min_cluster_a.merge_cluster(min_cluster_b)

            # print("Merging cluster {} into cluster {}; Distance: {}".format(min_cluster_b.cluster_id,
            #                                                                 min_cluster_a.cluster_id,
            #                                                                 min_cluster_distance_value))
            cluster_list.remove(min_cluster_b)

        return cluster_list

    def _compute_cluster_distances(self, cluster_list):

        cluster_distance_dict = dict()
        for cluster_a in cluster_list:

            cluster_distance_dict[cluster_a] = {}

            for cluster_b in cluster_list:
                distance = Cluster.complete_linkage_distance(cluster_a, cluster_b)

                # print("Distance between current cluster {} and cluster {} is {}".format(cluster_a.cluster_id,
                #                                                                         cluster_b.cluster_id,
                #                                                                         distance))
                cluster_distance_dict[cluster_a][cluster_b] = distance

        return cluster_distance_dict

    def print_clusters(self):

        for cluster, k in zip(self._cluster_list, range(len(self._cluster_list))):

            # logger.info("\n Nodes in cluster {}".format(k+1))

            for node in cluster.cluster_nodes:
                return

                # logger.info("\t Node: {}".format(node.name))


    def _get_prototypes(self):

        prototype_set = set()

        prototype_distance_map = dict()

        # Initalize prototype distance map, where the key is the prototype and the
        # value is that prototypes distance.
        # Note: The distance will be initialized to MAX_DISTANCE, which is the maximum distance
        prototype_distance_map = {key: value for (key, value) in
                                  [(cluster_node, MAX_DISTANCE) for cluster_node in self._cluster_node_list]}

        pass

        (curr_max_distance_cluster_node, current_max_distance_value) = self.compute_max_distance_from_prototype(
            prototype_distance_map)
        while True:

            # print("\nCurrent max distance: {}".format(current_max_distance_value))

            # All of the elements are less than 'MAX_DISTANCE_FROM_PROTOTYPE' away from a prototype
            if current_max_distance_value < MAX_DISTANCE_FROM_PROTOTYPE:
                break

            for cluster_node in self._cluster_node_list:

                if cluster_node == curr_max_distance_cluster_node or cluster_node in prototype_set:
                    continue

                # if the current distance from a prototype is greater than that of the curr_max_distance_analysis_report,
                # then we'll use the curr_max_distance_analysis_reports distance
                dist_from_curr_max_dist_cluster_node = ClusterNode.distance(curr_max_distance_cluster_node,
                                                                            cluster_node)

                if prototype_distance_map[cluster_node] > dist_from_curr_max_dist_cluster_node:
                    prototype_distance_map[cluster_node] = dist_from_curr_max_dist_cluster_node

                    # update the clusters  nodes nearest prototype
                    cluster_node.nearest_prototype_cluster_node = curr_max_distance_cluster_node

            # The current prototype candidate is its own prototype
            curr_max_distance_cluster_node.nearest_prototype_cluster_node = curr_max_distance_cluster_node

            # Add the current_prototype candidate to the prototype list
            prototype_set.add(curr_max_distance_cluster_node)

            # print("(Current total:{}) Added the following cluster node as prototype: {}".format(len(prototype_set),
                                                                                                # curr_max_distance_cluster_node.name))

            # Since the candidate is a prototype, its distance to a prototype is 0 because it is a prototype
            prototype_distance_map[curr_max_distance_cluster_node] = 0

            # Find the next potential prototype candidate
            (curr_max_distance_cluster_node, current_max_distance_value) = self.compute_max_distance_from_prototype(
                prototype_distance_map)

        return prototype_set

    @staticmethod
    def compute_max_distance_from_prototype(prototype_distance_map):

        """ Returns (key, value) tuple where the value is the max value in dictionary

        :param prototype_distance_map:
        :return: (key, value) tuple where the value is the max value in dictionary
        """

        max_distance = max(prototype_distance_map.items(), key=operator.itemgetter(1))

        return max_distance

    @staticmethod
    def get_min_cluster_distance(cluster_distance_dict):

        min_cluster_distance = None

        min_cluster_pair = ()

        for cluster_key_a in cluster_distance_dict:

            for cluster_key_b in cluster_distance_dict[cluster_key_a]:

                if cluster_key_a == cluster_key_b:
                    continue

                cluster_distance = cluster_distance_dict[cluster_key_a][cluster_key_b]

                if min_cluster_distance is None or min_cluster_distance > cluster_distance:
                    min_cluster_distance = cluster_distance
                    min_cluster_pair = (cluster_key_a, cluster_key_b)

        return (min_cluster_pair, min_cluster_distance)

    @property
    def cluster_list(self):
        return self._cluster_list


def bin_diff(binary_a_pb_file_path, binary_b_pb_file_path):
    dis_mnemonic_gen_a = DisassemblyMnemonicNgramGenerator.from_disassembly_file(binary_a_pb_file_path)
    dis_mnemonic_gen_b = DisassemblyMnemonicNgramGenerator.from_disassembly_file(binary_b_pb_file_path)

    cluster_node_a = ClusterNode(dis_mnemonic_gen_a)
    cluster_node_b = ClusterNode(dis_mnemonic_gen_b)

    similarity = ClusterNode.similarity(cluster_node_a, cluster_node_b)

    return similarity


def test_harness():
    TEST_DISASSEMBLY_A_PB_FILE_PATH = "disassembly_protos/explorer.exe_Disassembly_70506db080603a6a35004e92edb2ed5bfa51fac9e065e50b3640eb46ef528d48.pb.z"
    TEST_DISASSEMBLY_B_PB_FILE_PATH = "disassembly_protos/explorer_3416.exe_Disassembly_d5bc504277172be5c54b60ad5c13209dc1f729131def084de3ec8c72e54c58ef.pb.z"

    similarity = bin_diff(TEST_DISASSEMBLY_A_PB_FILE_PATH, TEST_DISASSEMBLY_B_PB_FILE_PATH)

    if round(similarity, 4) != .2268:
        # logger.warning("Expecting a similarity score of approximately .2268.  Actual score is {}".format(similarity))

        return

    approx_clustering = ApproxAgglomerativeClustering()

    # Load the dataset
    approx_clustering.load_binaries_from_directory("disassembly_protos/")

    start_time = time.time()
    approx_clustering.perform_clustering()
    elapsed_time = time.time() - start_time

    print("\nRuntime: {} seconds".format(elapsed_time))

    approx_clustering.print_clusters()

    pass


if __name__ == "__main__":
    test_harness()
