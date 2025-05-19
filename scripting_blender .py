import bpy
import math
import time

def ironhands_robotic_arm():
    obj = bpy.data.objects.get("Robotic Arm")  # Mets le nom de ton objet 3D ici
    if not obj:
        print("❌ Objet 'Robotic Arm' non trouvé.")
        return

    print("✅ Contrôle avec zone limitée activé.")

    scale_path = "C:/Users/HP/Desktop/Iron/scale.txt"  # Modifie le chemin si besoin
    rotate_path = "C:/Users/HP/Desktop/Iron/rotate.txt"
    pan_path = "C:/Users/HP/Desktop/Iron/pan.txt"

    move_factor = 0.1  # Vitesse de déplacement

    # 🧱 Limites de déplacement (zone de travail)
    min_x, max_x = -2.0, 2.0
    min_z, max_z = -2.0, 2.0

    while True:
        try:
            # Échelle (scale)
            with open(scale_path, 'r+') as f:
                val = f.read().strip()
                if val and val != "NULL":
                    s = float(val)
                    obj.scale = (s, s, s)
                    print(f"📦 Scale : {s}")
                    f.seek(0)
                    f.write("NULL")
                    f.truncate()

            # Rotation
            with open(rotate_path, 'r+') as f:
                val = f.read().strip()
                if val and val != "NULL":
                    deg = float(val)
                    obj.rotation_euler[2] += math.radians(deg)
                    print(f"🔁 Rotation Z += {deg}°")
                    f.seek(0)
                    f.write("NULL")
                    f.truncate()

            # Déplacement (pan) avec limites
            with open(pan_path, 'r+') as f:
                val = f.read().strip()
                if val and val != "NULL":
                    coords = val.split()
                    if len(coords) == 2:
                        dx = float(coords[0]) * move_factor
                        dz = float(coords[1]) * move_factor
                        new_x = obj.location.x + dx
                        new_z = obj.location.z + dz

                        # Appliquer seulement si dans la zone
                        if min_x <= new_x <= max_x:
                            obj.location.x = new_x
                        if min_z <= new_z <= max_z:
                            obj.location.z = new_z

                        print(f"🧭 X={obj.location.x:.2f}, Z={obj.location.z:.2f}")

                    f.seek(0)
                    f.write("NULL")
                    f.truncate()

            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            time.sleep(0.05)

        except Exception as e:
            print(f"⚠️ Erreur : {e}")
            time.sleep(0.1)

# ▶️ Lancer
ironhands_robotic_arm()
