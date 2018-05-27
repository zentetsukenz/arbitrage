workdir = $(shell pwd)

init: gen/trading/arbitrage

gen/trading/arbitrage:
	mkdir -p gen/trading/arbitrage

install: python elixir doc

# Python =====

python: gen/trading/arbitrage/python gen/trading/arbitrage/python/arbituer_pb2.py gen/trading/arbitrage/python/arbituer_pb2_grpc.py

gen/trading/arbitrage/python:
	mkdir -p gen/trading/arbitrage/python

gen/trading/arbitrage/python/arbituer_pb2.py:
	python -m grpc_tools.protoc -I. --python_out=gen/trading/arbitrage/python arbituer.proto

gen/trading/arbitrage/python/arbituer_pb2_grpc.py:
	python -m grpc_tools.protoc -I. --grpc_python_out=gen/trading/arbitrage/python arbituer.proto

# Elixr =====

elixir: gen/trading/arbitrage/elixir gen/trading/arbitrage/elixir/arbituer.pb.ex

gen/trading/arbitrage/elixir:
	mkdir -p gen/trading/arbitrage/elixir

gen/trading/arbitrage/elixir/arbituer.pb.ex:
	protoc --elixir_out=plugins=grpc:gen/trading/arbitrage/elixir arbituer.proto

# Document =====

doc: gen/trading/arbitrage/doc gen/trading/arbitrage/doc/index.html

gen/trading/arbitrage/doc:
	mkdir -p gen/trading/arbitrage/doc

gen/trading/arbitrage/doc/index.html:
	docker run --rm \
		-v $(workdir)/gen/trading/arbitrage/doc:/out \
		-v $(workdir):/protos \
		pseudomuto/protoc-gen-doc

# Utils =====

clean:
	rm -rf gen
