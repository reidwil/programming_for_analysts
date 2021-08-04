#!/bin/bash
# This is necessary for formatting github messages
echo '```'
git branch --show-current
diff-quality --violations sqlfluff --compare-branch=remotes/origin/develop
echo '```'
