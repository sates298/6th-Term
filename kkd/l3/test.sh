#!/usr/bin/env bash


clean() {
  rm -f *.dec *.stats *.out
}

testing() {
  modes=("omega" "gamma" "delta" "fibb")
  for f in ./*; do

    for m in "${modes[@]}"; do
      echo "$m:" >> $f.stats
      python ../lzw.py -e --$m -i  $f -o $f.$m.out >> $f.stats

      python ../lzw.py -d --$m -i $f.$m.out -o $f.$m.dec
      printf "$f $m "
      if cmp  $f $f.$m.dec > /dev/null 2>&1; then
        printf "[\033[1;32mPASS\033[m] \n"
      else
        printf "[\033[1;31mFAIL\033[m] \n"
      fi
    done
  done
}

cd tests
clean
${1-testing}
