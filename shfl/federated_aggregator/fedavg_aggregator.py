import numpy as np

from shfl.federated_aggregator.federated_aggregator import FederatedAggregator


class FedAvgAggregator(FederatedAggregator):
    """
    Implementation of Average Federated Aggregator. It only uses a simple average of the parameters of all the models.

    It implements [Federated Aggregator](../federated_aggregator/#federatedaggregator-class)
    """

    def aggregate_weights(self, clients_params):
        """
        Implementation of abstract method of class [AggregateWeightsFunction](../federated_aggregator/#federatedaggregator-class)
        # Arguments:
            clients_params: list of multi-dimensional (numeric) arrays. Each entry in the list contains the model's parameters of one client.

        # Returns
            aggregated_weights: aggregator weights representing the global learning model

        # References
            [Communication-Efficient Learning of Deep Networks from Decentralized Data](https://arxiv.org/abs/1602.05629)
        """

        clients_params_array = np.array(clients_params)
        shape = clients_params_array.shape[1]

        aggregated_weights = np.array([np.mean(clients_params_array[:, layer], axis=0) for layer in range(shape)])

        return aggregated_weights
