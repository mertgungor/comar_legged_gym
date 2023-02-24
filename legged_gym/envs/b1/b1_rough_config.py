from legged_gym.envs.b1.b1_flat_config import B1Cfg, B1CfgPPO


class B1RoughCfg(B1Cfg):
    class env(B1Cfg.env):
        num_envs = 6000  # 4096
        num_observations = 235

    class terrain(B1Cfg.terrain):
        measure_heights = True
        mesh_type = "trimesh"


    class init_state(B1Cfg.init_state):
        pass

    class control(B1Cfg.control):
        pass

    class commands(B1Cfg.commands):
        curriculum = False
        max_curriculum = 2.5

    class asset(B1Cfg.asset):
        pass

    class rewards(B1Cfg.rewards):
        pass


class B1RoughCfgPPO(B1CfgPPO):
    class policy:
        init_noise_std = 1.0
        actor_hidden_dims =  [512, 256, 128]
        critic_hidden_dims = [512, 256, 128]
        activation = 'elu'  # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid

    class runner(B1CfgPPO.runner):
        # logging
        run_name = 'b1_rough'
        experiment_name = 'b1_rough'

        max_iterations = 1500  # number of policy updates

        # load and resume
        # resume = True
        # load_run = -1 = last run
        # checkpoint = 1500 # -1 = last saved model
        # resume_path = None # updated from load_run and chkpt
