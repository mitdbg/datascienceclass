- Created spark cluster on EMR; students SSH to head node and submit jobs locally with spark-submit and --cluster-mode client
- Created EC2 instances for ray head (m5ad.2xlarge) and ray workers (4x m5.large)
  - used security group for head and worker nodes which opened ports: 6379, 8076, 8077, 8078, 10002-19999
  - ray head started with `export AUTOSCALER_MAX_NUM_FAILURES=inf; ulimit -n 65536; ray start --head --port=6379 --num-cpus=2 --resources='{"head": 1.0}' --object-store-memory 16000000000 --object-manager-port=8076 --node-manager-port 8077 --runtime-env-agent-port 8078 --dashboard-host=0.0.0.0`
  - ray workers started with `ray start --address='address-from-head:port' --resources='{"worker[1,2,3,4]": 1.0}' --object-store-memory 4000000000 --object-manager-port=8076 --node-manager-port 8077 --runtime-env-agent-port 8078`

when you port-forward to dashboard using: `ssh -NfL 8265:localhost:8265 hostname` you will need to access dashboard at http://0.0.0.0:8265 (i.e. not localhost or 127.0.0.1) 
