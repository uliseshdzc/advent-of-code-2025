
import sys
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d.art3d import Line3DCollection

sys.path.append("../advent-of-code-2025")

from day_08 import parse_input, find, union

INPUT = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

positions, edges, parent = parse_input(INPUT)
x, y, z = list(map(list, zip(*positions)))

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(projection='3d')
ax.grid(False)
ax.set_axis_off()

scatter = ax.scatter(x, y, z, s=20, c='tab:blue', depthshade=True)

# Only for initialization purposes
segments = [[positions[0], positions[0]]] 
temp_segments = [[positions[0], positions[0]]]

lc = Line3DCollection(segments, colors='tab:orange', linewidths=1.6, alpha=0.9)
lc2 = Line3DCollection(temp_segments, colors='tab:orange', linewidths=1.6, alpha=0.2)

ax.add_collection3d(lc)
ax.add_collection3d(lc2)


title = ax.set_title(f"Edges added: 0 | Remaining circuits: {len(positions)}")

def init():
    segments.clear()
    lc.set_segments(segments)
    title.set_text(f"Edges added: 0 | Remaining circuits: {len(positions)}")
    return [scatter, lc, lc2, title]

def update(step):
    a, b, remaining_circuits, added_edges, should_stick = step
    title.set_text(f"Edges added: {added_edges} | Remaining circuits: {remaining_circuits}")
    temp_segments.clear()
    if should_stick:
        segments.append([positions[a], positions[b]])
    else:     
        temp_segments.append([positions[a], positions[b]])

def union_steps():
    remaining_circuits = len(positions)
    for a, b in edges:
        if find(a, parent) == find(b, parent) and remaining_circuits > 1:
            yield a, b, remaining_circuits - 1, len(positions) - remaining_circuits, False            
            continue

        union(a, b, parent)
        remaining_circuits -= 1
        if remaining_circuits == 0:
            return 
        
        yield a, b, remaining_circuits - 1, len(positions) - remaining_circuits, True

anim = animation.FuncAnimation(
    fig,
    update,
    init_func=init,
    frames=union_steps(),
    interval=600,   
    cache_frame_data=False
)

plt.show()