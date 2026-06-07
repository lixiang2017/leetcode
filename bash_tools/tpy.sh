#! /bin/bash

# quick touch a file with a given question name from leetcode

join_with_underscore() {
  local IFS=_
  echo "$*"
}

normalize_leetcode_no() {
  local no="$1"
  if [[ "$no" =~ ^([0-9]+)\.?$ ]]; then
    no="${BASH_REMATCH[1]}"
  else
    echo "Invalid leetcode problem no: $no" >&2
    return 1
  fi
  printf "%04d.0" "$no"
}

normalize_codeforces_no() {
  local no="$1"
  if [[ "$no" =~ ^([0-9]{1,4})([A-Za-z]?)$ ]]; then
    printf "%04d%s" "${BASH_REMATCH[1]}" "${BASH_REMATCH[2]}"
  else
    echo "Invalid Codeforces problem no: $no" >&2
    return 1
  fi
}

create_file_if_missing() {
  local file="$1"
  touch "$file"
}

open_with_editor() {
  local file="$1"
  if command -v code >/dev/null 2>&1; then
    code "$file"
  elif command -v st >/dev/null 2>&1; then
    st "$file"
  fi
}

touch_explore_file() {
  local ext="$1"
  shift
  local name
  name="$(join_with_underscore "$@")"
  local file="${name}${ext}"

  echo "touch a file here"
  echo "the number of arguments is $#"
  echo "all parameters are $*"
  echo "filename: $file"
  create_file_if_missing "$file"
  echo "touch a file $file done."
}

touch_problem_file() {
  local ext="$1"
  shift
  local number="$1"
  shift
  local normalized
  normalized="$(normalize_leetcode_no "$number")" || return 1
  local suffix
  suffix="$(join_with_underscore "$@")"
  local file="${normalized}${suffix:+_${suffix}}${ext}"

  echo "touch a file here"
  echo "the number of arguments is $#"
  echo "all parameters are $number $*"
  echo "filename: $file"
  create_file_if_missing "$file"
  echo "touch a file $file done."
  open_with_editor "$file"
}

touch_codeforces_file() {
  local ext="$1"
  shift
  local number="$1"
  shift
  local normalized
  normalized="$(normalize_codeforces_no "$number")" || return 1
  local suffix
  suffix="$(join_with_underscore "$@")"
  local file="${normalized}${suffix:+_${suffix}}${ext}"

  echo "touch a file here"
  echo "the number of arguments is $#"
  echo "all parameters are $number $*"
  echo "filename: $file"
  create_file_if_missing "$file"
  echo "touch a file $file done."
  open_with_editor "$file"
}

texpy() { touch_explore_file .py "$@"; }
tprpy() { touch_problem_file .py "$@"; }
texcpp() { touch_explore_file .cpp "$@"; }
tprcpp() { touch_problem_file .cpp "$@"; }
tprc() { touch_problem_file .c "$@"; }
texjava() { touch_explore_file .java "$@"; }
tprjava() { touch_problem_file .java "$@"; }
texgo() { touch_explore_file .go "$@"; }
tprgo() { touch_problem_file .go "$@"; }
texjs() { touch_explore_file .js "$@"; }
tprjs() { touch_problem_file .js "$@"; }
tprsql() { touch_problem_file .sql "$@"; }
tprcs() { touch_problem_file .cs "$@"; }
tprrust() { touch_problem_file .rs "$@"; }
texsql() { touch_explore_file .sql "$@"; }
tcfpy() { touch_codeforces_file .py "$@"; }
