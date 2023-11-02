[GitHub](https://github.com/opencurve/curve) | [Chinese README](https://github.com/opencurve/curve/blob/master/README_cn.md)  
Curve是网易主导自研的现代化存储系统，可以提供高可靠性、高可扩展性、高性能的数据存储服务，目前支持文件存储(CurveFS)和块存储(CurveBS)。

+ pre：
	+ C++
	+ Distribute：
		+ 分布式存储相关：GFS，Ceph
		+ 一致性协议：比如Raft
	+ RPC（curve使用的是bRPC）

+ [How to compile](https://github.com/opencurve/curve/blob/master/docs/cn/build_and_run.md)（use bazel）
+ main doc：
	+ [core code interpretation](https://github.com/opencurve/curve/wiki/Curve%E6%BA%90%E7%A0%81%E5%8F%8A%E6%A0%B8%E5%BF%83%E6%B5%81%E7%A8%8B%E6%B7%B1%E5%BA%A6%E8%A7%A3%E8%AF%BB)
	+ 概念：**[mds](https://github.com/opencurve/curve/blob/master/docs/cn/mds.md)** | [chunk server](https://github.com/opencurve/curve/blob/master/docs/cn/chunkserver_design.md) | [Client](https://github.com/opencurve/curve/blob/master/docs/cn/curve-client.md)
+ [main meetup](https://github.com/opencurve/curve-meetup-slides/tree/main/2020)

## CurveAdm
[GitHub](https://github.com/opencurve/curveadm) | [wiki](https://github.com/opencurve/curveadm/wiki)  
CurveAdm是Curve团队为提高系统易用性而设计的工具，其主要用于快速部署和运维CurveBS/CurveFS集群。

### Deploy

+ [bs](https://github.com/opencurve/curve/blob/master/README_cn.md#curvebs-%E5%BF%AB%E9%80%9F%E4%BD%93%E9%AA%8C)
	+ [All-in-one](https://github.com/opencurve/curveadm/wiki/curvebs-cluster-deployment)
+ [fs](https://github.com/opencurve/curve/blob/master/README_cn.md#curvefs-%E5%BF%AB%E9%80%9F%E4%BD%93%E9%AA%8C)


[Tutor](https://github.com/opencurve/curve/blob/master/README_cn.md#%E9%83%A8%E7%BD%B2all-in-one%E4%BD%93%E9%AA%8C%E7%8E%AF%E5%A2%83)

### Maintain
```bash
curveadm status  # 查看集群状态, 包括集群ID和所属Container ID
curveadm enter ID

curveadm stop --id ID  # 停止服务, 不提供参数id则通配所有
curveadm clean --id ID  # 清理服务(清楚数据)，不提供参数id则通配所有
```

## CurveTool
截止到2023.03.03，正在将旧工具`curve_ops_tool`（C++）向新工具`curve`（Golang）重构（[进度](https://github.com/opencurve/curve/tree/master/tools-v2#comparison-of-old-and-new-commands)）

### v1
[source code](https://github.com/opencurve/curve/tree/master/src/tools) | [use guide](https://github.com/opencurve/curve/blob/master/docs/cn/curve_ops_tool.md)

### v2
[source code](https://github.com/opencurve/curve/tree/master/tools-v2) | [Intor](https://github.com/opencurve/curve/blob/master/docs/cn/curve%E5%B7%A5%E5%85%B7.md) | [develop guide](https://github.com/opencurve/curve/blob/master/tools-v2/docs/zh/develop.md)

### Develop

#### reset-peer
`curve_ops_tool reset-peer` -> `curve bs update peer`

```bash
curve_ops_tool check-copyset -logicalPoolId=1 -copysetId=1 --detail 
# 查看集群状态

curve_ops_tool reset-peer -logicalPoolId=1 -copysetId=1 -peer=10.246.159.82:8202:0 --new_conf=10.246.159.82:8202:0 -max_retry=3 -timeout_ms=100

./curve bs update peer 10.246.159.82:8202:0 --logicalpoolid=1 --copysetid=1 --rpcretrytimes=1 --rpctimeout=10s
```

+ Test:

# Use
