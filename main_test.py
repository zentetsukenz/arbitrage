import time
import unittest

import grpc
import grpc_testing

import main
import arbitrage_pb2

ARBITRAGE_SERVICE = arbitrage_pb2.DESCRIPTOR.services_by_name[
    'ArbitrageService']


class ArbitrageServiceServicerTest(unittest.TestCase):
    def setUp(self):
        self._real_time = grpc_testing.strict_real_time()
        self._fake_time = grpc_testing.strict_fake_time(time.time())

        service = main.ArbitrageServiceServicer()
        descriptors_to_servicers = {ARBITRAGE_SERVICE: service}

        self._real_time_server = grpc_testing.server_from_dictionary(
            descriptors_to_servicers, self._real_time)
        self._fake_time_server = grpc_testing.server_from_dictionary(
            descriptors_to_servicers, self._fake_time)

    def test_initialize_returns_context(self):
        rpc = self._real_time_server.invoke_unary_unary(
            ARBITRAGE_SERVICE.methods_by_name['Initialize'], (),
            arbitrage_pb2.InitializeRequest(
                basic=arbitrage_pb2.BasicRequest(),
                buying_exchange=arbitrage_pb2.messages_dot_exchange__pb2.
                Exchange(name=arbitrage_pb2.messages_dot_exchange__pb2.
                         _EXCHANGE_NAME.values_by_name['BXINTH'].number),
                selling_exchange=arbitrage_pb2.messages_dot_exchange__pb2.
                Exchange(name=arbitrage_pb2.messages_dot_exchange__pb2.
                         _EXCHANGE_NAME.values_by_name['BITFINEX'].number),
                trading_pair=arbitrage_pb2.messages_dot_trading__pair__pb2.
                TradingPair(
                    base_currency='omg',
                    quote_currency='eth',
                ),
                enter_points=[
                    arbitrage_pb2.TradingPoint(gap=1.0, amount=10),
                    arbitrage_pb2.TradingPoint(gap=2.0, amount=20)
                ],
                exit_points=[arbitrage_pb2.TradingPoint(gap=-5.0, amount=100)],
                slippage_allowance=2.0), None)
        initial_metadata = rpc.initial_metadata()
        response, trailing_metadata, code, details = rpc.termination()

        self.assertEqual(
            arbitrage_pb2.InitializeResponse(
                basic=arbitrage_pb2.BasicResponse(),
                context=arbitrage_pb2.Context(
                    buying_exchange=arbitrage_pb2.messages_dot_exchange__pb2.
                    Exchange(name=arbitrage_pb2.messages_dot_exchange__pb2.
                             _EXCHANGE_NAME.values_by_name['BXINTH'].number),
                    selling_exchange=arbitrage_pb2.messages_dot_exchange__pb2.
                    Exchange(name=arbitrage_pb2.messages_dot_exchange__pb2.
                             _EXCHANGE_NAME.values_by_name['BITFINEX'].number),
                    trading_pair=arbitrage_pb2.messages_dot_trading__pair__pb2.
                    TradingPair(
                        base_currency='omg',
                        quote_currency='eth',
                    ),
                    enter_points=[
                        arbitrage_pb2.TradingPoint(gap=1.0, amount=10),
                        arbitrage_pb2.TradingPoint(gap=2.0, amount=20)
                    ],
                    exit_points=[
                        arbitrage_pb2.TradingPoint(gap=-5.0, amount=100)
                    ],
                    slippage_allowance=2.0)), response)
        self.assertIs(code, grpc.StatusCode.OK)


if __name__ == '__main__':
    unittest.main(verbosity=2)
