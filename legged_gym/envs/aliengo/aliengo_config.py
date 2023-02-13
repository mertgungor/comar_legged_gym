
from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg,LeggedRobotCfgPPO


class AliengoFlatCfg( LeggedRobotCfg ):
    class init_state( LeggedRobotCfg.init_state ):
        pos = [0.0, 0.0, 0.38]  # x,y,z [m]
        default_joint_angles = {  # = target angles [rad] when action = 0.0
            "FL_hip_joint": 0.1,  # [rad]
            "RL_hip_joint": 0.1,  # [rad]
            "FR_hip_joint": -0.1,  # [rad]
            "RR_hip_joint": -0.1,  # [rad]

            "FL_thigh_joint": 0.8,  # [rad]
            "RL_thigh_joint": 1.0,  # [rad]
            "FR_thigh_joint": 0.8,  # [rad]
            "RR_thigh_joint": 1.0,  # [rad]

            "FL_calf_joint": -1.5,  # [rad]
            "RL_calf_joint": -1.5,  # [rad]
            "FR_calf_joint": -1.5,  # [rad]
            "RR_calf_joint": -1.5,  # [rad]
            }  # [rad]
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.25
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4

    class control( LeggedRobotCfg.control ):
        # PD Drive parameters:
        control_type = 'P'
        stiffness = {'joint': 100.0}  # [N*m/rad]
        damping = {'joint': 1.6}     # [N*m*s/rad]
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.25
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4

    class asset( LeggedRobotCfg.asset ):
        file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/aliengo/urdf/aliengo.urdf'
        name = "aliengo"
        foot_name = "calf"
        penalize_contacts_on = ["thigh", "calf"]
        terminate_after_contacts_on = ["base", "hip"]
        self_collisions = 1
        fix_base_link = True
        disable_gravity = True
    class rewards( LeggedRobotCfg.rewards ):
        soft_dof_pos_limit = 0.9

        class scales( LeggedRobotCfg.rewards.scales ):
            termination = 0.0
            #tracking_lin_vel = 1
            #tracking_ang_vel = 0.5
            #lin_vel_z = -2.0
            #ang_vel_xy = -0.05
            #torques = -1e-5
            dof_pos_limits = -5.0
            #dof_acc = -2.5e-7
            feet_air_time = 1.5
            collision = -5e-2
            #action_rate = -0.01

    class env( LeggedRobotCfg.env ):
        num_observations = 48

    class terrain( LeggedRobotCfg.terrain ):
        mesh_type = 'plane'
        measure_heights = False
        curriculum = True

class AliengoFlatCfgPPO( LeggedRobotCfgPPO ):
    class algorithm( LeggedRobotCfgPPO.algorithm ):
        entropy_coef = 0.01
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = ''
        experiment_name = 'go1_flat'
        
        resume = False
        load_run = -1 # -1 = last run
        checkpoint = -1 # -1 = last saved model
        resume_path = None # updated from load_run and chkpt
    class policy( LeggedRobotCfgPPO.policy):
 
        # actor_hidden_dims =  [128, 64, 32]
        # critic_hidden_dims = [128, 64, 32]

        activation = 'elu' # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
