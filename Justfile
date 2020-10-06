build-docker:
  mkdir -p benchmark/build
  poetry export -f requirements.txt > benchmark/build/requirements.txt
  docker build -t edax-enchmark ./benchmark

bench to="/dev/null":
  python benchmark/profiling.py | tee -a {{to}}
