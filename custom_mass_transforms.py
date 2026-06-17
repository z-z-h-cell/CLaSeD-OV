from mmseg.registry import TRANSFORMS
from mmcv.transforms import BaseTransform
import numpy as np

@TRANSFORMS.register_module()
class BinarizeMassachusettsBuilding(BaseTransform):
    """
    Transforms [0,0,0], [255,255,255] RGB masks into 2D indices [0, 1].
    """
    def transform(self, results):
        if 'gt_seg_map' in results:
            mask = results['gt_seg_map']
            if len(mask.shape) == 3:
                # take max over channels robustly handles Red, White, or any RGB color versus Black
                mask = np.max(mask, axis=2)
                
            # robust binarization: map ANY non-zero value to index 1
            mask = mask.copy()  # ensure it's modifiable
            mask[mask > 0] = 1
            mask = mask.astype(np.uint8)
            results['gt_seg_map'] = mask
        return results
