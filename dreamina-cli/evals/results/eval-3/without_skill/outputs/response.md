# 全能参考模式任务执行结果

我需要帮你使用全能参考模式生成视频。请先检查以下文件是否存在：
- 主图：D:\素材\主图.png
- 运镜参考视频：D:\素材\运镜参考.mp4
- 背景音乐：D:\素材\音乐.mp3

如果文件都存在，请执行以下命令：

```bash
dreamina multimodal2video --image "D:\素材\主图.png" --video "D:\素材\运镜参考.mp4" --audio "D:\素材\音乐.mp3" --prompt="根据参考视频的运镜方式，配合音乐节奏，将静态图片转为动态视频" --model_version=seedance2.0 --duration=8 --ratio=16:9 --poll=180
```

这个任务需要约 3-5 分钟，请耐心等待。