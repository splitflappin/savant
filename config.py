pa_flag_dict = {"field_out":1,"nan":0,"strikeout":1,"double":1,"strikeout_double_play":1,
                "single":1,"force_out":1,"hit_by_pitch":1,"grounded_into_double_play":1,
                "home_run":1,"walk":1,"caught_stealing_2b":0,"sac_bunt":1,"triple":1,
                "sac_fly":1,"field_error":1,"double_play":1,"catcher_interf":1,"fielders_choice_out":1,
                "fielders_choice":1,"pickoff_1b":0,"other_out":0,"caught_stealing_home":0,"pickoff_caught_stealing_2b":0,
                "caught_stealing_3b":0,"sac_fly_double_play":1,"pickoff_caught_stealing_home":0,"pickoff_2b":0,"run":0,
                "triple_play":1,"batter_interference":1,"pickoff_3b":0,"sac_bunt_double_play":1,"pickoff_caught_stealing_3b":0}

ab_flag_dict = {"field_out":1,"nan":0,"strikeout":1,"double":1,
                "strikeout_double_play":1,"single":1,"force_out":1,"hit_by_pitch":0,
                "grounded_into_double_play":1,"home_run":1,"walk":0,"caught_stealing_2b":0,
                "sac_bunt":0,"triple":1,"sac_fly":0,"field_error":1,
                "double_play":1,"catcher_interf":0,"fielders_choice_out":1,"fielders_choice":1,
                "pickoff_1b":0,"other_out":0,"caught_stealing_home":0,"pickoff_caught_stealing_2b":0,
                "caught_stealing_3b":0,"sac_fly_double_play":1,"pickoff_caught_stealing_home":0,"pickoff_2b":0,
                "run":0,"triple_play":1,"batter_interference":1,"pickoff_3b":0,"sac_bunt_double_play":1,"pickoff_caught_stealing_3b":0}

is_hit_dict = {"field_out":0,"nan":0,"strikeout":0,"double":1,"strikeout_double_play":0,
                "single":1,"force_out":0,"hit_by_pitch":0,"grounded_into_double_play":0,"home_run":1,
                "walk":0,"caught_stealing_2b":0,"sac_bunt":0,"triple":1,"sac_fly":0,
                "field_error":0,"double_play":0,"catcher_interf":0,"fielders_choice_out":0,"fielders_choice":0,
                "pickoff_1,b":0,"other_out":0,"caught_stealing_home":0,"pickoff_caught_stealing_2b":0,"caught_stealing_3b":0,
                "sac_fly_double_play":0,"pickoff_caught_stealing_home":0,"pickoff_2b":0,"run":0,"triple_play":0,"batter_interference":0,
                "pickoff_3b":0,"sac_bunt_double_play":0,"pickoff_caught_stealing_3b":0}

swing_dict = {"ball":0,"foul_tip":1,"called_strike":0,"swinging_strike":1, "pitchout": 0, "bunt_foul_tip": 1,
                "foul":1,"hit_into_play_no_out":1,"hit_into_play":1,"hit_into_play_score":1, "missed_bunt": 1,
                "hit_by_pitch":0,"blocked_ball":0,"swinging_strike_blocked":1, "foul_bunt": 1}

fair_contact_dict = {"ball":0,"foul_tip":0,"called_strike":0,"swinging_strike":0, "pitchout": 0,
                "foul":0,"hit_into_play_no_out":1,"hit_into_play":1, "missed_bunt": 0,
                "hit_into_play_score":1,"hit_by_pitch":0, "bunt_foul_tip": 0,
                "blocked_ball":0,"swinging_strike_blocked":0, "foul_bunt": 0}

foul_contact_dict = {"ball":0,"foul_tip":0,"called_strike":0,"swinging_strike":0, "pitchout": 0,
                "foul":1,"hit_into_play_no_out":1,"hit_into_play":1, "missed_bunt": 0,
                "hit_into_play_score":1,"hit_by_pitch":0, "bunt_foul_tip": 0,
                "blocked_ball":0,"swinging_strike_blocked":0, "foul_bunt": 1}

inplay_dict = {"ball":0,"foul_tip":0,"called_strike":0,"swinging_strike":0, "pitchout": 0, "bunt_foul_tip": 0,
              "foul":0,"hit_into_play_no_out":1,"hit_into_play":1,"hit_into_play_score":1,  "missed_bunt": 0,
              "hit_by_pitch":0,"blocked_ball":0,"swinging_strike_blocked":0, "foul_bunt": 0}

isoutdict = {"field_out":1, "strikeout":1,"grounded_into_double_play":2,
             "sac_bunt":1,"fielders_choice_out":1, "fielders_choice":0,
             "force_out":1,"caught_stealing_3b":1,"caught_stealing_2b":1, "double_play":2,
             "strikeout_double_play":2,"sac_fly_double_play":2, "sac_fly":1,
             "other_out":1,"pickoff_caught_stealing_3b":1,"triple_play":3,
             "pickoff_1b":1,"sac_bunt_double_play":2,"caught_stealing_home":1,
             "pickoff_2b":1,"pickoff_3b":1}

my_des_dict = {"ball": "Ball", "hit_into_play": "In Play", "called_strike": "Called Strike",
          "foul": "Foul", "swinging_strike": "Whiff", "blocked_ball": "Ball",
          "swinging_strike_blocked": "Whiff", "foul_tip": "Foul", "foul_bunt": "Foul",
          "missed_bunt": "whiff", "pitchout": "Ball", "bunt_foul_tip": "Foul"}