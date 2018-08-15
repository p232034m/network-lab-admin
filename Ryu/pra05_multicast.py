from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet


class ExampleSwitch13(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(ExampleSwitch13, self).__init__(*args, **kwargs)
        # initialize mac address table.
        self.mac_to_port = {}

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        self.logger.info("hello datapathID %s",datapath.id)
        
        port_1 = 1
        port_2 = 2
        port_3 = 3

        actions_1 = [parser.OFPActionOutput(port=port_1)]
        actions_2 = [parser.OFPActionOutput(port=port_2)]
        actions_3 = [parser.OFPActionOutput(port=port_3)]

        buckets = [parser.OFPBucket(actions=actions_1),parser.OFPBucket(actions=actions_2),
                parser.OFPBucket(actions=actions_3)]

        group_id = 1
        req = parser.OFPGroupMod(datapath, ofproto.OFPGC_ADD, ofproto.OFPGT_ALL, group_id,buckets)
        datapath.send_msg(req)

        
        match = parser.OFPMatch()
        actions = [parser.OFPActionGroup(group_id = group_id)]
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,actions)]
        mod = parser.OFPFlowMod(datapath=datapath, priority=10,match=match,instructions=inst,command=ofproto.OFPFC_ADD)
        
        self.logger.info(mod)

        datapath.send_msg(mod)
    
        """
        # install the table-miss flow entry.
        match = parser.OFPMatch(in_port=1)
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        self.add_flow(datapath, 10, match, actions)
        """
    
    def add_flow(self, datapath, priority, match, actions):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # construct flow_mod message and send it.
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
        mod = parser.OFPFlowMod(datapath=datapath, priority=priority,
                                match=match, instructions=inst)
        self.logger.info("flow send")
        datapath.send_msg(mod)
    