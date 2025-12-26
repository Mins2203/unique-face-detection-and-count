import math


class Tracker:
    def __init__(self):
       
        self.center_points = {}
       
        self.id_count = 0
        
        
        self.lost_frames = {}
        
        self.max_lost_frames = 30


    def update(self, objects_rect):
        objects_bbs_ids = []

        new_objects_centers = []
        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2
            new_objects_centers.append([x, y, w, h, cx, cy])

        if len(self.center_points) == 0:
            for obj in new_objects_centers:
                x, y, w, h, cx, cy = obj
                self.register_object(x, y, w, h, cx, cy, objects_bbs_ids)
            return objects_bbs_ids

        used_existing_ids = set()
        used_new_indices = set()
        
        
        for object_id, center in self.center_points.items():
            min_dist = float('inf')
            match_index = -1
            
            for i, new_obj in enumerate(new_objects_centers):
                if i in used_new_indices:
                    continue
                
                _, _, _, _, cx, cy = new_obj
                dist = math.hypot(cx - center[0], cy - center[1])
                
                if dist < 80 and dist < min_dist:  
                    min_dist = dist
                    match_index = i
            
            if match_index != -1:
                
                x, y, w, h, cx, cy = new_objects_centers[match_index]
                self.center_points[object_id] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, object_id])
                
                self.lost_frames[object_id] = 0
                
                used_existing_ids.add(object_id)
                used_new_indices.add(match_index)
            else:
                
                self.lost_frames[object_id] += 1

        
        for i, new_obj in enumerate(new_objects_centers):
            if i not in used_new_indices:
                x, y, w, h, cx, cy = new_obj
                self.register_object(x, y, w, h, cx, cy, objects_bbs_ids)

        self.clean_up_ids()

        return objects_bbs_ids

    def register_object(self, x, y, w, h, cx, cy, objects_bbs_ids):
        self.center_points[self.id_count] = (cx, cy)
        self.lost_frames[self.id_count] = 0
        objects_bbs_ids.append([x, y, w, h, self.id_count])
        self.id_count += 1

    def clean_up_ids(self):
        new_center_points = {}
        new_lost_frames = {}
        
        for object_id in self.center_points:
            if self.lost_frames[object_id] <= self.max_lost_frames:
                new_center_points[object_id] = self.center_points[object_id]
                new_lost_frames[object_id] = self.lost_frames[object_id]
        
        self.center_points = new_center_points.copy()
        self.lost_frames = new_lost_frames.copy()