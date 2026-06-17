# Third-Party Notices

This repository contains original CLaSeD-OV code together with third-party
components needed for inference.

## SAM 3

The `sam3/` directory is derived from Meta Segment Anything Model 3 (SAM 3)
materials and is subject to Meta's SAM License, not the Apache License 2.0
used for the original CLaSeD-OV code.

Official repository: https://github.com/facebookresearch/sam3

SAM 3 license: https://github.com/facebookresearch/sam3/blob/main/LICENSE

A local copy of the SAM License is included at `SAM_LICENSE`.

The SAM 3 checkpoint weights are not included in this repository. Users must
obtain the checkpoint from an official or otherwise authorized source and
follow the applicable SAM 3 license and checkpoint terms.

## OpenMMLab

This project uses the OpenMMLab segmentation stack, including MMEngine, MMCV,
and MMSegmentation. Please follow their upstream licenses and installation
instructions.

MMEngine: https://github.com/open-mmlab/mmengine

MMCV: https://github.com/open-mmlab/mmcv

MMSegmentation: https://github.com/open-mmlab/mmsegmentation
