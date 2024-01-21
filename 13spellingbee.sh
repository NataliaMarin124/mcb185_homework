gunzip -c dictionary.gz | grep "r" | grep -v "[^roziacn]" | grep -E ".{4,}"
