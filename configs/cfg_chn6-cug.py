_base_ = './base_config.py'

# model settings
model = dict(
    classname_path='./configs/cls_chn6-cug.txt',
    prob_thd=0.35,
    confidence_threshold=0.55,
)

# dataset settings
dataset_type = 'CHN6_CUGDataset'
data_root = 'data/CHN6-CUG'

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    dict(type='PackSegInputs')
]

test_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        data_prefix=dict(
            img_path='CHN6-CUG/image_cvt',
            seg_map_path='CHN6-CUG/label_cvt'),
        pipeline=test_pipeline))
