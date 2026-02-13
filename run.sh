#!/bin/sh

cd ./scripts

test -f "config-mapping.yaml" || cp "config-mapping_sample.yaml" "config-mapping.yaml"
test -f "config-mapping.yaml" || echo "Missing sample config: config-mapping_sample.yaml"
test -f "config-mapping.yaml" || exit 1

test -f "config-mqtt.yaml" || cp "config-mqtt_sample.yaml" "config-mqtt.yaml"
test -f "config-mqtt.yaml" || echo "Missing sample config: config-mqtt_sample.yaml"
test -f "config-mqtt.yaml" || exit 1

python3  ./script.py
