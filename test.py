import torch
print('='*50)
print('✅ PyTorch 版本:', torch.__version__)
print('✅ CUDA 是否可用:', torch.cuda.is_available())
if torch.cuda.is_available():
    print('✅ CUDA 版本:', torch.version.cuda)
    print('✅ GPU 名称:', torch.cuda.get_device_name(0))
print('='*50)

# 检查所有核心包
import importlib
packages = [
    'transformers', 'datasets', 'evaluate', 'peft',
    'accelerate', 'gradio', 'optimum', 'sentencepiece',
    'sklearn', 'pandas', 'matplotlib', 'tensorboard',
    'nltk', 'rouge', 'jupyterlab'
]
for p in packages:
    try:
        lib = importlib.import_module(p)
        if hasattr(lib, '__version__'):
            print(f'✅ {p:15s} 版本：{lib.__version__}')
        else:
            print(f'✅ {p:15s} 正常导入')
    except:
        print(f'❌ {p:15s} 导入失败！')
print('='*50)
print('🎉 全部检查完成！')