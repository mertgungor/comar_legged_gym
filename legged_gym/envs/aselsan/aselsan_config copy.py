from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO

class AselsanCfg( LeggedRobotCfg ):
    class init_state( LeggedRobotCfg.init_state ):
        pos = [0.0, 0.0, 0.42] # x,y,z [m]
        default_joint_angles = { # = target angles [rad] when action = 0.0
            
            "comar/abad_1_joint" :  0.1,  # [rad]
            "comar/abad_2_joint" :  0.1,  # [rad]
            "comar/abad_3_joint" : -0.1,  # [rad]
            "comar/abad_4_joint" : -0.1,  # [rad]
            
            "comar/hip_1_joint"  :  0.8,  # [rad]
            "comar/hip_2_joint"  :  1.,  # [rad]
            "comar/hip_3_joint"  :  0.8,  # [rad]
            "comar/hip_4_joint"  :  1.,  # [rad]

            "comar/knee_1_joint" : -1.62,  # [rad]
            "comar/knee_2_joint" : -1.62,  # [rad]
            "comar/knee_3_joint" : -1.62,  # [rad]
            "comar/knee_4_joint" : -1.62,  # [rad]
        }

    class env( LeggedRobotCfg.env ):
        num_observations = 48
    
    class terrain( LeggedRobotCfg.terrain ):
        mesh_type       = 'plane'
        measure_heights = False

    class asset( LeggedRobotCfg.asset ):
        file                        = '{LEGGED_GYM_ROOT_DIR}/resources/robots/comar/urdf/comar.urdf'
        flip_visual_attachments     = False
        foot_name                   = "knee"
        terminate_after_contacts_on = ["base", "hip"]
        penalize_contacts_on        = ["knee", "hip"]
        self_collisions             = 1 # 1 to disable, 0 to enable...bitwise filter
        # fix_base_link               = True
        # disable_gravity             = True

    class control( LeggedRobotCfg.control ):
        # PD Drive parameters:
        control_type = 'P'
        stiffness    = {'joint': 20.}  # [N*m/rad]
        damping      = {'joint': 0.5}     # [N*m*s/rad]
        action_scale = 0.25
        decimation   = 4

    class rewards( LeggedRobotCfg.rewards ):
        soft_dof_pos_limit = 0.9
        base_height_target = 0.5
        class scales( LeggedRobotCfg.rewards.scales ):
            torques          = -0.0002
            dof_pos_limits   = -5.0
            base_height      = -1.0
            collision        = -5e-2  # default -1.
            feet_air_time    =  1.   # default 1.
            # ang_vel_xy       =  -0.08 # -0.05
            # tracking_lin_vel = 1.5 # 1
            # tracking_ang_vel = 0.7 # 0.5
    

  

class AselsanCfgPPO( LeggedRobotCfgPPO ):
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = ''
        experiment_name = 'comar_flat'

    class policy( LeggedRobotCfgPPO.policy):
        actor_hidden_dims  = [128, 64, 32]
        critic_hidden_dims = [128, 64, 32]
        activation = 'elu' # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid

    class runner( LeggedRobotCfgPPO.runner):
        max_iterations = 300
  