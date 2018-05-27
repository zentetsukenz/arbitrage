defmodule Trading.Arbitrage.BasicRequest do
  @moduledoc false
  use Protobuf, syntax: :proto3

  @type t :: %__MODULE__{
          context: Trading.Arbitrage.Context.t()
        }
  defstruct [:context]

  field :context, 1, type: Trading.Arbitrage.Context
end

defmodule Trading.Arbitrage.BasicResponse do
  @moduledoc false
  use Protobuf, syntax: :proto3

  @type t :: %__MODULE__{
          context: Trading.Arbitrage.Context.t()
        }
  defstruct [:context]

  field :context, 1, type: Trading.Arbitrage.Context
end

defmodule Trading.Arbitrage.InitializeRequest do
  @moduledoc false
  use Protobuf, syntax: :proto3

  @type t :: %__MODULE__{
          basic: Trading.Arbitrage.BasicRequest.t()
        }
  defstruct [:basic]

  field :basic, 1, type: Trading.Arbitrage.BasicRequest
end

defmodule Trading.Arbitrage.InitializeResponse do
  @moduledoc false
  use Protobuf, syntax: :proto3

  @type t :: %__MODULE__{
          basic: Trading.Arbitrage.BasicResponse.t()
        }
  defstruct [:basic]

  field :basic, 1, type: Trading.Arbitrage.BasicResponse
end

defmodule Trading.Arbitrage.HandleDataRequest do
  @moduledoc false
  use Protobuf, syntax: :proto3

  @type t :: %__MODULE__{
          basic: Trading.Arbitrage.BasicRequest.t(),
          buying_exchange: Trading.Arbitrage.ExchangeData.t(),
          selling_exchange: Trading.Arbitrage.ExchangeData.t()
        }
  defstruct [:basic, :buying_exchange, :selling_exchange]

  field :basic, 1, type: Trading.Arbitrage.BasicRequest
  field :buying_exchange, 2, type: Trading.Arbitrage.ExchangeData
  field :selling_exchange, 3, type: Trading.Arbitrage.ExchangeData
end

defmodule Trading.Arbitrage.HandleDataResponse do
  @moduledoc false
  use Protobuf, syntax: :proto3

  @type t :: %__MODULE__{
          basic: Trading.Arbitrage.BasicResponse.t(),
          command: Trading.Arbitrage.Command.t()
        }
  defstruct [:basic, :command]

  field :basic, 1, type: Trading.Arbitrage.BasicResponse
  field :command, 2, type: Trading.Arbitrage.Command
end

defmodule Trading.Arbitrage.AnalysisRequest do
  @moduledoc false
  use Protobuf, syntax: :proto3

  @type t :: %__MODULE__{
          basic: Trading.Arbitrage.BasicRequest.t()
        }
  defstruct [:basic]

  field :basic, 1, type: Trading.Arbitrage.BasicRequest
end

defmodule Trading.Arbitrage.AnalysisResponse do
  @moduledoc false
  use Protobuf, syntax: :proto3

  @type t :: %__MODULE__{
          basic: Trading.Arbitrage.BasicResponse.t()
        }
  defstruct [:basic]

  field :basic, 1, type: Trading.Arbitrage.BasicResponse
end

defmodule Trading.Arbitrage.Context do
  @moduledoc false
  use Protobuf, syntax: :proto3

  @type t :: %__MODULE__{
          buying_exchange: String.t(),
          selling_exchange: String.t(),
          trading_pair: String.t(),
          entry_points: [Trading.Arbitrage.TradingPoint.t()],
          exit_points: [Trading.Arbitrage.TradingPoint.t()],
          slippage_allowance: float
        }
  defstruct [
    :buying_exchange,
    :selling_exchange,
    :trading_pair,
    :entry_points,
    :exit_points,
    :slippage_allowance
  ]

  field :buying_exchange, 1, type: :string
  field :selling_exchange, 2, type: :string
  field :trading_pair, 3, type: :string
  field :entry_points, 4, repeated: true, type: Trading.Arbitrage.TradingPoint
  field :exit_points, 5, repeated: true, type: Trading.Arbitrage.TradingPoint
  field :slippage_allowance, 6, type: :float
end

defmodule Trading.Arbitrage.TradingPoint do
  @moduledoc false
  use Protobuf, syntax: :proto3

  @type t :: %__MODULE__{
          gap: float,
          amount: float
        }
  defstruct [:gap, :amount]

  field :gap, 1, type: :float
  field :amount, 2, type: :float
end

defmodule Trading.Arbitrage.ExchangeData do
  @moduledoc false
  use Protobuf, syntax: :proto3

  @type t :: %__MODULE__{
          name: String.t(),
          trading_pair: String.t(),
          data: Trading.Arbitrage.BarData.t()
        }
  defstruct [:name, :trading_pair, :data]

  field :name, 1, type: :string
  field :trading_pair, 2, type: :string
  field :data, 3, type: Trading.Arbitrage.BarData
end

defmodule Trading.Arbitrage.BarData do
  @moduledoc false
  use Protobuf, syntax: :proto3

  @type t :: %__MODULE__{
          open: float,
          close: float,
          high: float,
          low: float,
          volume: float
        }
  defstruct [:open, :close, :high, :low, :volume]

  field :open, 1, type: :float
  field :close, 2, type: :float
  field :high, 3, type: :float
  field :low, 4, type: :float
  field :volume, 5, type: :float
end

defmodule Trading.Arbitrage.Command do
  @moduledoc false
  use Protobuf, syntax: :proto3

  @type t :: %__MODULE__{
          action: integer,
          amount: float,
          buying_price: float,
          selling_price: float
        }
  defstruct [:action, :amount, :buying_price, :selling_price]

  field :action, 1, type: Trading.Arbitrage.Command.Action, enum: true
  field :amount, 2, type: :float
  field :buying_price, 3, type: :float
  field :selling_price, 4, type: :float
end

defmodule Trading.Arbitrage.Command.Action do
  @moduledoc false
  use Protobuf, enum: true, syntax: :proto3

  field :NONE, 0
  field :ENTER, 1
  field :EXIT, 2
end

defmodule Trading.Arbitrage.ArbitrageService.Service do
  @moduledoc false
  use GRPC.Service, name: "trading.arbitrage.ArbitrageService"

  rpc :Initialize, Trading.Arbitrage.InitializeRequest, Trading.Arbitrage.InitializeResponse
  rpc :HandleData, Trading.Arbitrage.HandleDataRequest, Trading.Arbitrage.HandleDataResponse
  rpc :Analysis, Trading.Arbitrage.AnalysisRequest, Trading.Arbitrage.AnalysisResponse
end

defmodule Trading.Arbitrage.ArbitrageService.Stub do
  @moduledoc false
  use GRPC.Stub, service: Trading.Arbitrage.ArbitrageService.Service
end
