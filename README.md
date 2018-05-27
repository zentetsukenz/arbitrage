# Arbitrage service definition

A definition for implementing an arbitrage service. Please note that the service is not responsible for executing a trade command.

# Flow

The flow is similar to what [catalyst](https://github.com/enigmampc/catalyst) is doing. However, instead of doing everything inside one script, I've decided to separate the service and the controller, so that we can extend it easier.

### To summarize,

1. Client call initialize RPC to initialize a trading context.
2. For each price ticker, a client call handles data RPC.
3. Client call analyses for a performance matrix (Not implemented yet).

# Document

Please visit [document](https://zentetsukenz.github.io/arbituer)

# Usage

```
make install
```

This command should generate document, Elixir code and Python code.
