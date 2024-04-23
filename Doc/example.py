from BRCI.BRCI_RF import *
from BRCI import *

if __name__ == "__main__":
    data = BRCI()
    data.project_name = 'no_name'
    data.project_display_name = 'no_name'
    data.project_folder_directory = os.path.join(os.getcwd(), 'Projects')
    data.debug_logs = ['time']
    data.write_blank = False

    def stress_test(bricks: int, size: float = 200.0, generate: bool = True) -> None:
        import random
        data.project_name = f'stress_test_{bricks}'
        data.project_display_name = f'Stress Test ({bricks}b / {size}m)'
        for brick_id_st in range(bricks):
            new_brick_st = create_brick(
                brick="DoubleSiren_1x2x1s",
                position=[random.uniform(0.0, size), random.uniform(0.0, size), random.uniform(0.0, size)],
                rotation=[random.uniform(0.0, 360.0), random.uniform(0.0, 360.0), random.uniform(0.0, 360.0)])

            for property_st in new_brick_st.keys():
                if isinstance(new_brick_st[property_st], float):
                    new_brick_st[property_st] = random.uniform(-1_000_000_000.0, 1_000_000_000.0)

            data.add_brick(str(brick_id_st), new_brick_st)

        if generate:
            data.write_preview()
            data.write_metadata()
            data.write_brv()
            data.write_to_br()
    # --------------------------------------------------

    stress_test(10)