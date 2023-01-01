_base_ = './damo_yolo_s.py'

model = dict(
    type='DAMOYOLODetector',
    data_preprocessor=dict(
        type='mmdet.DetDataPreprocessor',
        mean=[0., 0., 0.],
        std=[1., 1., 1.],
        bgr_to_rgb=True),
    backbone=dict(type='TinyNAS_csp',
                  out_indices=(2, 3, 4),
                  with_spp=True,
                  use_focus=True,
                  act='silu',
                  reparam=True,
                  backbone_structure='m',
                  ),
    neck=dict(type='GiraffeNeckv2',
              depth=1.5,
              hidden_ratio=1.0,
              in_channels=[128, 256, 512],
              out_channels=[128, 256, 512],
              act='silu',
              spp=False,
              block_name='BasicBlock_3x3_Reverse',
              ),
    bbox_head=dict(type='ZeroHead',
                   num_classes=80,
                   in_channels=[128, 256, 512],
                   stacked_convs=0,
                   reg_max=16,
                   act='silu',
                   nms_conf_thre=0.05,
                   nms_iou_thre=0.7
                   ))
