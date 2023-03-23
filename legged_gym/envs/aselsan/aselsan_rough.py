from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO

class AselsanRoughCfg( LeggedRobotCfg ):
    class init_state( LeggedRobotCfg.init_state ):
        pos = [0.0, 0.0, 0.42] # x,y,z [m]
        default_joint_angles = { # = target angles [rad] when action = 0.0
            
            "comar/abad_1_joint" :  0.1,  # [rad]
            "comar/abad_2_joint" :  0.1,  # [rad]
            "comar/abad_3_joint" : -0.1,  # [rad]
            "comar/abad_4_joint" : -0.1,  # [rad]
            
            "comar/hip_1_joint"  :  0.8,  # [rad]
            "comar/hip_2_joint"  :  1.0, # [rad]
            "comar/hip_3_joint"  :  0.8,  # [rad]
            "comar/hip_4_joint"  :  1.0, # [rad]

            "comar/knee_1_joint" : -1.5,   # [rad]
            "comar/knee_2_joint" : -1.5,   # [rad]
            "comar/knee_3_joint" : -1.5,   # [rad]
            "comar/knee_4_joint" : -1.5,   # [rad]
        }

    class env( LeggedRobotCfg.env ):
        num_observations = 235
    
    class terrain( LeggedRobotCfg.terrain ):
        mesh_type       = 'trimesh'
        measure_heights = False

    class asset( LeggedRobotCfg.asset ):
        file                        = '{LEGGED_GYM_ROOT_DIR}/resources/robots/comar/urdf/comar_a1.urdf'
        flip_visual_attachments     = False
        foot_name                   = "knee"
        terminate_after_contacts_on = ["base"]
        penalize_contacts_on        = ["knee", "hip"]
        self_collisions             = 1 # 1 to disable, 0 to enable...bitwise filter
        # fix_base_link               = True
        # disable_gravity             = True

    class control( LeggedRobotCfg.control ):
        # PD Drive parameters:
        control_type = 'P'
        stiffness    = {'joint': 40}  # [N*m/rad]
        damping      = {'joint': 1}     # [N*m*s/rad]
        action_scale = 0.25
        decimation   = 4

    # class rewards:
    #     class scales:
    #         termination = -0.0
    #         tracking_lin_vel = 1.0
    #         tracking_ang_vel = 0.5
    #         lin_vel_z = -2.0
    #         ang_vel_xy = -0.05
    #         orientation = -0.
    #         torques = -0.00001
    #         dof_vel = -0.
    #         dof_acc = -2.5e-7
    #         base_height = -0. 
    #         feet_air_time =  1.0
    #         collision = -1.
    #         feet_stumble = -0.0 
    #         action_rate = -0.01
    #         stand_still = -0.

    #     only_positive_rewards = True # if true negative total rewards are clipped at zero (avoids early termination problems)
    #     tracking_sigma = 0.25 # tracking reward = exp(-error^2/sigma)
    #     soft_dof_pos_limit = 1. # percentage of urdf limits, values above this limit are penalized
    #     soft_dof_vel_limit = 1.
    #     soft_torque_limit = 1.
    #     base_height_target = 1.
    #     max_contact_force = 100. # forces above this value are penalized

    class rewards( LeggedRobotCfg.rewards ):
        soft_dof_pos_limit = 0.9
        base_height_target = 0.4
        class scales( LeggedRobotCfg.rewards.scales ):

            base_height      = -1.0
            collision        = -5e-2 # default -1.
            feet_air_time    =  1.0



class AselsanRoughCfgPPO( LeggedRobotCfgPPO ):
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = ''
        experiment_name = 'comar_flat'

    class policy( LeggedRobotCfgPPO.policy):
        actor_hidden_dims  = [512, 256, 128]
        critic_hidden_dims = [512, 256, 128]
        activation = 'elu' # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid

    class runner( LeggedRobotCfgPPO.runner):
        max_iterations = 1500
  