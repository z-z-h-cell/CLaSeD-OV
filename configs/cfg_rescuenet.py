_base_ = './base_config.py'

# model settings
model = dict(
    classname_path='./configs/cls_rescuenet.txt',
    confidence_threshold=0.5,
    prob_thd=0.75,
)

# dataset settings
dataset_type = 'RescueNetDataset'
data_root = 'data/RescueNet'

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
        reduce_zero_label=False,
        data_prefix=dict(
            img_path='test-org-img',
            seg_map_path='test-label-img'),
        pipeline=test_pipeline))
