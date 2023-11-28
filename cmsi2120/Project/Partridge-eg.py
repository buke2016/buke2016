import matplotlib.pyplot as plt
%matplotlib inline

import peartree as pt

path = '../ac_transit_gtfs.zip'

# Automatically identify the busiest day and
# read that in as a Partidge feed
feed = pt.get_representative_feed(path)

# Set a target time period to
# use to summarize impedance
start = 7*60*60  # 7:00 AM
end = 10*60*60  # 10:00 AM

# Converts feed subset into a directed
# network multigraph
G = pt.load_feed_as_graph(feed, start, end)
fig, ax = pt.generate_plot(G)