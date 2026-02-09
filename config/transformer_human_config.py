from yacs.config import CfgNode as CN


class ConfigStereoHuman:
    def __init__(self):
        self.cfg = CN()
        self.cfg.name = ''
        self.cfg.stage1_ckpt = None
        self.cfg.restore_ckpt = None
        self.cfg.lr = 0.0
        self.cfg.wdecay = 0.0
        self.cfg.batch_size = 0
        self.cfg.num_steps = 0

        self.cfg.dataset = CN()
        self.cfg.dataset.anchor = False
        self.cfg.dataset.source_id = None
        self.cfg.dataset.train_novel_id = None
        self.cfg.dataset.val_novel_id = None
        self.cfg.dataset.use_hr_img = None
        self.cfg.dataset.use_processed_data = None
        self.cfg.dataset.data_root = ''
        # gsussian render settings
        self.cfg.dataset.bg_color = [0, 0, 0]
        self.cfg.dataset.zfar = 100.0
        self.cfg.dataset.znear = 0.01
        self.cfg.dataset.trans = [0.0, 0.0, 0.0]
        self.cfg.dataset.scale = 1.0
        self.cfg.dataset.refine = False #whether to use refinement

        self.cfg.record = CN()
        self.cfg.record.ckpt_path = None
        self.cfg.record.show_path = None
        self.cfg.record.logs_path = None
        self.cfg.record.file_path = None
        self.cfg.record.loss_freq = 0
        self.cfg.record.eval_freq = 0

        #unimatch setting
        self.cfg.unimatch = CN()
        self.cfg.unimatch.unimatch_ckpt = None
        self.cfg.unimatch.inference_size = None
        self.cfg.unimatch.pred_bidir_disp = None
        self.cfg.unimatch.padding_factor =0
        self.cfg.unimatch.upsample_factor = 0
        self.cfg.unimatch.num_scales = 0
        self.cfg.unimatch.attn_type = None
        self.cfg.unimatch.attn_splits_list = None
        self.cfg.unimatch.corr_radius_list = None
        self.cfg.unimatch.prop_radius_list = None
        self.cfg.unimatch.num_reg_refine = 0
        self.cfg.unimatch.feature_channels = 0
        self.cfg.unimatch.num_head = 0
        self.cfg.unimatch.ffn_dim_expansion = 0
        self.cfg.unimatch.num_transformer_layers = 0
        self.cfg.unimatch.reg_refine = None
        self.cfg.unimatch.task = None

        self.cfg.raft = CN()
        self.cfg.raft.mixed_precision = None
        self.cfg.raft.train_iters = 0
        self.cfg.raft.val_iters = 0
        self.cfg.raft.corr_implementation = 'reg_cuda'  # or 'reg'
        self.cfg.raft.corr_levels = 4
        self.cfg.raft.corr_radius = 4
        self.cfg.raft.n_downsample = 3
        self.cfg.raft.n_gru_layers = 1
        self.cfg.raft.slow_fast_gru = None
        self.cfg.raft.encoder_dims = [64, 96, 128]
        self.cfg.raft.hidden_dims = [128]*3

        self.cfg.gsnet = CN()
        self.cfg.gsnet.encoder_dims = None
        self.cfg.gsnet.decoder_dims = None
        self.cfg.gsnet.parm_head_dim = None


    def get_cfg(self):
        return self.cfg.clone()
    
    def load(self, config_file):
        self.cfg.defrost()
        self.cfg.merge_from_file(config_file)
        self.cfg.freeze()

def create_config(cap_config):
    cfg = ConfigStereoHuman()
    cfg.load(cap_config)
    cfg = cfg.get_cfg()
    return cfg