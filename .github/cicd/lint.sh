#!/bin/bash
# This is necessary for formatting github messages
echo '```'
diff-quality --violations sqlfluff --compare-branch=remotes/origin/develop
echo '```'
