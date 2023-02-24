from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO

class AselsanCfg( LeggedRobotCfg ):
    class init_state( LeggedRobotCfg.init_state ):
        pos = [0.0, 0.0, 0.42] # x,y,z [m]
        default_joint_angles = { # = target angles [rad] when action = 0.0
            
            "abad_1_joint" :  0.0,  # [rad]
            "abad_2_joint" :  0.0,  # [rad]
            "abad_3_joint" :  0.0,  # [rad]
            "abad_4_joint" :  0.0,  # [rad]
            
            "hip_1_joint"  :  0.0,  # [rad]
            "hip_2_joint"  :  0.0,  # [rad]
            "hip_3_joint"  :  0.0,  # [rad]
            "hip_4_joint"  :  0.0,  # [rad]

            "knee_1_joint" : -0.0,  # [rad]
            "knee_2_joint" : -0.0,  # [rad]
            "knee_3_joint" : -0.0,  # [rad]
            "knee_4_joint" : -0.0,  # [rad]
        }

    class env( LeggedRobotCfg.env ):
        num_observations = 48
    
    class terrain( LeggedRobotCfg.terrain ):
        mesh_type = 'plane'
        measure_heights = False

    class asset( LeggedRobotCfg.asset ):
        file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/aselsan/urdf/comar_generated.urdf'
        flip_visual_attachments = False

class AselsanCfgPPO( LeggedRobotCfgPPO ):
    pass
  