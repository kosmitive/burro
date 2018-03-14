class Agent:
    """Represents an interface for one agent. Different implementations
    can be used as this will be used inside the simulation to drive the
    different goods."""

    def get_outgoing_orders(self, pos, clen, stock, orders):
        """
        This method should calculate outgoing orders. Therefore several information is
        about itself is available.

        :param pos: The position in the product flow, where 0 means first node.
        :param clen: The length of the chain, for getting position in order flow.
        :param stock: The supply available in the stock.
        :param orders: The deliveries requested by the node (pos + 1)
        :return: How much should be ordered from (pos - 1)
        """
        return 42
