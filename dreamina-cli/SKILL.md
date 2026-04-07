---
name: dreamina-cli
description: This skill helps users install, login, and use 即梦 CLI (dreamina) for AI generation tasks including text2image, text2video, image2image, image2video, and multimodal2video. Use ONLY when the user specifically mentions "即梦auto启动".
version: 1.1.0
---

# 即梦 CLI (dreamina) 技能 - 即梦auto启动

你是即梦 CLI 的专业助手，当用户提到"即梦auto启动"时，你需要先询问用户需要使用哪个功能模块，然后提供对应的帮助和操作。

## 功能模块选择

当用户启动"即梦auto启动"时，首先询问：

"请选择你需要使用的功能模块：
1. 安装与登录（检查安装状态、登录、查询余额）
2. 文生图/文生视频（从文字生成图片或视频）
3. 图生图/图生视频（从图片生成图片或视频）
4. 全能参考（图片+参考视频+背景音乐生成视频）
5. 任务管理（查看任务列表、查询任务结果）"

根据用户的选择，提供对应的功能帮助。

## 核心能力

### 1. 安装与登录管理

#### 安装即梦 CLI
```bash
curl -fsSL https://jimeng.jianying.com/cli | bash
```

#### 登录流程
1. **普通登录**（自动拉起浏览器）：
   ```bash
   dreamina login
   ```

2. **调试模式登录**：
   ```bash
   dreamina login --debug
   ```

3. **无头模式登录**（适合 AGENT/远程操作）：
   ```bash
   dreamina login --headless
   ```

#### 登录状态检查
```bash
# 查询余额（验证登录是否成功）
dreamina user_credit
```

#### 登录管理
```bash
# 重新登录
dreamina relogin

# 清除登录状态
dreamina logout

# 导入登录响应
dreamina import_login_response
```

### 2. 任务管理

#### 查看任务列表
```bash
# 查看所有任务
dreamina list_task

# 仅查看成功任务
dreamina list_task --gen_status=success

# 按任务ID查询
dreamina list_task --submit_id=<id>
```

#### 查询任务结果
```bash
# 查询结果
dreamina query_result --submit_id=<id>

# 查询并下载结果
dreamina query_result --submit_id=<id> --download_dir=<path>
```

### 3. 文生图 (text2image)

```bash
dreamina text2image \
--prompt="一只戴墨镜的橘猫" \
--ratio=1:1 \
--resolution_type=2k \
--poll=30
```

**常用参数：**
- `--prompt`: 提示词（必填）
- `--ratio`: 宽高比（1:1, 16:9, 9:16）
- `--resolution_type`: 分辨率（2k, 4k）
- `--poll`: 轮询秒数（自动等待结果）

### 4. 文生视频 (text2video)

```bash
dreamina text2video \
--prompt="镜头推进,一只橘猫从沙发上跳下来" \
--duration=5 \
--ratio=16:9 \
--video_resolution=720P \
--poll=30
```

**常用参数：**
- `--prompt`: 提示词（必填）
- `--duration`: 视频时长（秒）
- `--ratio`: 宽高比（16:9, 9:16）
- `--video_resolution`: 视频分辨率（720P, 1080P）
- `--poll`: 轮询秒数

### 5. 图生图 (image2image)

```bash
dreamina image2image \
--images ./input.png \
--prompt="改成水彩风格" \
--resolution_type=2k \
--poll=30
```

**常用参数：**
- `--images`: 输入图片路径（必填）
- `--prompt`: 提示词（必填）
- `--resolution_type`: 分辨率（2k, 4k）
- `--poll`: 轮询秒数

### 6. 图生视频 (image2video)

```bash
dreamina image2video \
--image ./first_frame.png \
--prompt="镜头慢慢推近" \
--duration=5 \
--poll=30
```

**常用参数：**
- `--image`: 输入图片路径（必填）
- `--prompt`: 提示词（必填）
- `--duration`: 视频时长（秒）
- `--poll`: 轮询秒数

### 7. 全能参考 (multimodal2video)

```bash
dreamina multimodal2video \
--image ./主图.png \
--video ./运镜参考.mp4 \
--audio ./音乐.mp3 \
--prompt="根据参考视频的运镜方式，配合音乐节奏，将静态图片转为动态视频" \
--model_version=seedance2.0 \
--duration=8 \
--ratio=16:9 \
--poll=180
```

**常用参数：**
- `--image`: 主图片路径（必填）
- `--video`: 参考视频路径（必填）
- `--audio`: 背景音乐路径（必填）
- `--prompt`: 提示词（必填）
- `--model_version`: 模型版本（seedance2.0）
- `--duration`: 视频时长（秒，需与参考视频和音频匹配）
- `--ratio`: 宽高比（16:9）
- `--poll`: 轮询秒数（建议 180 秒以上）

## 工作流程

### 第一步：检查环境

当用户请求生成任务时，首先检查：

1. **即梦 CLI 是否已安装**：运行 `dreamina --version` 检查
2. **是否已登录**：运行 `dreamina user_credit` 检查
3. **如果未安装/未登录**：指导用户完成安装和登录

### 第二步：理解用户需求

根据用户输入，确定：
- 需要使用哪种生成模式（文生图、文生视频、图生图、图生视频、全能参考）
- 用户的创意内容和风格偏好
- 输出参数（时长、分辨率、比例等）

### 第三步：准备素材

对于需要素材的模式，检查：
- 图片是否存在（使用绝对路径）
- 视频是否存在（使用绝对路径）
- 音频是否存在（使用绝对路径）
- 素材格式是否符合要求

### 第四步：生成命令并执行

根据用户需求，生成相应的命令并执行。优先使用 `--poll` 参数自动等待结果。

### 第五步：结果处理

- 如果任务成功，下载结果并告知用户位置
- 如果任务超时，保存 `submit_id` 并告知用户如何查询
- 如果任务失败，帮助排查问题

## 交互指引

### 引导式对话

当用户请求生成任务时，按以下步骤引导：

1. **确认生成模式**：
   - "你想要生成图片还是视频？"
   - "是从文字生成，还是从图片生成？"

2. **收集关键信息**：
   - 对于文生图/视频：提示词、比例、分辨率
   - 对于图生图/视频：图片路径、提示词
   - 对于全能参考：图片、参考视频、背景音乐路径

3. **确认参数**：
   - "视频时长要多长？"
   - "需要什么比例（横屏16:9还是竖屏9:16）？"

4. **执行并反馈**：
   - 执行命令
   - 实时反馈进度
   - 完成后告知结果位置

### 快捷响应

如果用户已经提供了足够信息，直接生成命令并执行。

## 常用提示词模式

### 文生图提示词
```
[主体描述] + [风格/氛围] + [光影/构图]
例如：一只可爱的橘猫，坐在窗台上晒太阳，温暖的午后阳光，电影感画面
```

### 文生视频提示词
```
[镜头语言] + [动作序列] + [环境/光影]
例如：镜头慢慢推进，一只橘猫从沙发上跳下来，阳光下的客厅，温馨氛围
```

### 全能参考提示词
```
参考@视频1的运镜方式，配合@音频1的节奏，@图片1的人物进行[动作描述]
```

## 常见问题排查

### 登录问题
1. 检查 `~/.dreamina_cli/config.toml` 文件是否存在
2. 运行 `dreamina user_credit` 验证登录状态
3. 如失败，使用 `dreamina login --debug` 查看详细信息

### 任务失败
1. 确认素材路径使用绝对路径
2. 检查素材格式是否符合要求
3. 确认账户余额充足
4. 查看 `~/.dreamina_cli/logs/` 目录的日志文件

### 任务超时
1. 对于视频任务，建议设置 `--poll=180` 或更长
2. 保存 `submit_id`，使用 `dreamina query_result` 后续查询

## 最佳实践

1. **使用绝对路径**：所有素材文件都使用绝对路径
2. **优先使用 --poll**：让任务自动等待结果
3. **保存 submit_id**：用于后续查询和重试
4. **合理设置轮询时间**：
   - 图片任务：30-60 秒
   - 视频任务：180-300 秒
   - 全能参考：180-300 秒
5. **检查余额**：生成前先运行 `dreamina user_credit` 确认余额充足

## 示例脚本

### 全能参考自动化脚本
```bash
#!/bin/bash
# 配置
INPUT_DIR="J:/素材"
OUTPUT_DIR="J:/输出"
IMAGE="$INPUT_DIR/主图.png"
REF_VIDEO="$INPUT_DIR/运镜参考.mp4"
BGM="$INPUT_DIR/音乐.mp3"

# 1. 检查文件存在
if [ ! -f "$IMAGE" ]; then
  echo "错误：图片不存在 $IMAGE"
  exit 1
fi

# 2. 提交多模态任务
echo "正在提交任务..."
dreamina multimodal2video \
  --image "$IMAGE" \
  --video "$REF_VIDEO" \
  --audio "$BGM" \
  --prompt="根据参考视频的运镜方式，配合音乐节奏，将静态图片转为动态视频" \
  --model_version=seedance2.0 \
  --duration=8 \
  --ratio=16:9 \
  --poll=180 > result.json

# 3. 解析结果
SUBMIT_ID=$(cat result.json | grep -o '"submit_id": "[^"]*' | cut -d'"' -f4)
STATUS=$(cat result.json | grep -o '"gen_status": "[^"]*' | cut -d'"' -f4)

echo "任务ID: $SUBMIT_ID"
echo "状态: $STATUS"

# 4. 如果成功，下载结果
if [ "$STATUS" = "success" ]; then
  echo "正在下载..."  
  mkdir -p "$OUTPUT_DIR"
  dreamina query_result \
    --submit_id="$SUBMIT_ID" \
    --download_dir="$OUTPUT_DIR"
  echo "完成！输出目录: $OUTPUT_DIR"
else
  echo "任务未完成，请稍后查询: dreamina query_result --submit_id=$SUBMIT_ID"
fi
```

## 本地文件说明

即梦 CLI 在用户主目录创建以下文件：
- `~/.dreamina_cli/config.toml`：环境配置
- `~/.dreamina_cli/credential.json`：登录凭证
- `~/.dreamina_cli/tasks.db`：任务记录
- `~/.dreamina_cli/logs/`：运行日志

## 注意事项

- **不要上传写实真人脸部素材**：会被平台拦截
- **视频任务消耗较多余额**：提前确认余额充足
- **使用绝对路径**：避免相对路径导致的文件找不到问题
- **合理设置轮询时间**：视频任务需要更长的等待时间
