#!/usr/bin/env python
from context_predeployed.context_generator import ContextGenerator
import json


def main():
    print(json.dumps(ContextGenerator().get_abi(), sort_keys=True, indent=4))


if __name__ == '__main__':
    main()
