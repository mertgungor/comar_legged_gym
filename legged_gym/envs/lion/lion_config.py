from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO

class LionCfg( LeggedRobotCfg ):
    class init_state( LeggedRobotCfg.init_state ):
        pos = [0.0, 0.0, 0.55] # x,y,z [m]
        default_joint_angles = { # = target angles [rad] when action = 0.0
            'JointFR_abad':  0.0,   # [rad]
            'JointFL_abad':  0.0,   # [rad]
            'JointHR_abad':  0.0,  # [rad]
            'JointHL_abad':  0.0,   # [rad]
 
            'JointFR_hip' :  0.0,     # [rad]
            'JointFL_hip' :  0.0,   # [rad]
            'JointHR_hip' :  0.0,     # [rad]
            'JointHL_hip' :  0.0,   # [rad]

            'JointFR_knee': -0.0,   # [rad]
            'JointFL_knee': -0.0,    # [rad]
            'JointHR_knee': -0.0,  # [rad]
            'JointHL_knee': -0.0    # [rad]

        }

    class env( LeggedRobotCfg.env ):
        num_observations = 48
    
    class terrain( LeggedRobotCfg.terrain ):
        mesh_type = 'plane'
        measure_heights = False

    class asset( LeggedRobotCfg.asset ):
        file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/lion/urdf/lion.urdf'
        flip_visual_attachments = False


class LionCfgPPO( LeggedRobotCfgPPO ):
    pass
  