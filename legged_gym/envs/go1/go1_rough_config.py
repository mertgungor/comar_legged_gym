from legged_gym.envs.go1.go1_flat_config import Go1Cfg, Go1CfgPPO


class Go1RoughCfg(Go1Cfg):
    class env(Go1Cfg.env):
        num_envs = 6000  # 4096
        num_observations = 235

    class terrain(Go1Cfg.terrain):
        measure_heights = True
        mesh_type = "trimesh"


    class init_state(Go1Cfg.init_state):
        pass

    class control(Go1Cfg.control):
        pass

    class commands(Go1Cfg.commands):
        curriculum = False
        max_curriculum = 2.5

    class asset(Go1Cfg.asset):
        pass

    class rewards(Go1Cfg.rewards):
        pass


class Go1RoughCfgPPO(Go1CfgPPO):
    class policy:
        init_noise_std = 1.0
        actor_hidden_dims =  [512, 256, 128]
        critic_hidden_dims = [512, 256, 128]
        activation = 'elu'  # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid

    class runner(Go1CfgPPO.runner):
        # logging
        run_name = 'go1_rough'
        experiment_name = 'go1_rough'

        max_iterations = 10000  # number of policy updates

        # load and resume
        # resume = True
        # load_run = -1 = last run
        # checkpoint = 1500 # -1 = last saved model
        # resume_path = None # updated from load_run and chkpt
