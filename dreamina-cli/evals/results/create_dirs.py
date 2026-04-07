import os
import sys

workspace_dir = r"D:\AI\AIcode\.claude\skills\dreamina-cli\workspace\iteration-1"

for i in range(1, 6):
    eval_dir = os.path.join(workspace_dir, f"eval-{i}")

    with_skill_dir = os.path.join(eval_dir, "with_skill", "outputs")
    without_skill_dir = os.path.join(eval_dir, "without_skill", "outputs")

    for dir_path in [with_skill_dir, without_skill_dir]:
        if not os.path.exists(dir_path):
            try:
                os.makedirs(dir_path, exist_ok=True)
                print(f"Created directory: {dir_path}")
            except Exception as e:
                print(f"Error creating directory {dir_path}: {e}")

print("Directory creation completed!")