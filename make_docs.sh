#!/bin/bash
set -e
BOOK=../book/docs
if [ -d $BOOK ] ; then
  cp -ru $BOOK/shared docs/
  cp -ru $BOOK/copyright.rst docs/
fi
