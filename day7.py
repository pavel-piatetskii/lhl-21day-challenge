# example dicitonary
user_boxes = {'weight': [4, 2, 18, 21, 14, 13],
              'box_name': ['box1', 'box2', 'box3', 'box4', 'box5', 'box6']
              }

def sorting_boxes(weights, boxes):
  box_order = []
  weights_sorted = sorted(weights)
  for weight in weights_sorted:
    box_order.append(boxes[weights.index(weight)])
  return box_order

print(sorting_boxes(user_boxes['weight'], user_boxes['box_name']))