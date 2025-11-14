select "rusher_player_name" as player, "rusher_player_id" as player_id, COUNT(*) as rushing_tds
from nfl_pbp
where "rush_touchdown" = 1 and rush = 1
group by "rusher_player_name", "rusher_player_id"
having COUNT(*) > 0
order by rushing_tds desc;