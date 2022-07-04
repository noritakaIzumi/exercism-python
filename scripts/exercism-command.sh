#!/usr/bin/env bash

sudo cp -v exercism /usr/local/bin/
rm -v exercism

pushd /workspace
ln -vnfs exercism-python python
exercism configure --token=${EXERCISM_TOKEN} --workspace=${PWD}
popd
