import networkx as nx


def hierarchical_layout(G: nx.Graph) -> tuple:
    """Function to create dictionary with positions of nodes with hierarchical
    arrangement.

    Paramaters:
    -----------
    G: nx.Graph
        NetworkX Graph object

    Returns:
    (int, int, dict)
        Tuple with canvas size for the loan and non-loan, and a dictionary with
        the node as key and the position as coordinate list or tuple
    """

    # Record shortest distance between node pairs (to evaluate hierarchy levels)
    spl = dict(nx.all_pairs_shortest_path_length(G))

    # Count number of nodes for agg, sub1, sub2 levels
    agg = []
    sub1 = []
    sub2 = []
    for node in list(G.nodes()):
        if spl['CA'][node] == 2:
            agg.append(node)
        elif spl['CA'][node] == 3:
            sub1.append(node)
        elif spl['CA'][node] == 4:
            sub2.append(node)

    # Attribute agg, sub1, sub2 containers to loan or non-loan
    loan = []
    non_loan = []
    for node in list(G.nodes()):
        if spl['01'][node] > spl['02'][node]:
            non_loan.append(node)
        else:
            loan.append(node)

    # Resize canvas based on how many nodes are present (loan)
    largest_row_loan = max(
        [
            len([x for x in agg if x in loan]),
            len([x for x in sub1 if x in loan]), 
            len([x for x in sub2 if x in loan]),
        ]
    )
    if largest_row_loan > 4:
        canvas_loan_size = 0.25 * largest_row_loan
    else:
        canvas_loan_size = 1
    
    # Resize canvas based on how many nodes are present (non-loan)
    largest_row_nonloan = max(
        [
            len([x for x in agg if x in non_loan]),
            len([x for x in sub1 if x in non_loan]), 
            len([x for x in sub2 if x in non_loan]),
        ]
    )
    print(f'Max row NON-LOAN: {largest_row_nonloan}')
    if largest_row_nonloan > 4:
        canvas_nonloan_size = 0.3 * largest_row_loan
    else:
        canvas_nonloan_size = 1

    # Define canvas size for lower levels
    canvas_loan_size_sub1 = canvas_loan_size / len([x for x in agg if x in loan])
    canvas_loan_size_sub2 = canvas_loan_size / len([x for x in sub1 if x in loan])
    canvas_nonloan_size_sub1 = canvas_nonloan_size / len([x for x in agg if x in non_loan])
    canvas_nonloan_size_sub2 = canvas_nonloan_size / len([x for x in sub1 if x in non_loan])

    # Assign x, y coordinates to nodes
    agg_loan_iter = 0
    agg_nonloan_iter = 0
    position = {}
    
    # CA, sections, and agg-fac
    for node in list(G.nodes()):
        if node == 'CA':
            x, y = 0, 0.8
        elif node == '01':
            x, y = -0.5, 0.4
        elif node == '02':
            x, y = 0.5, 0.4
        else:
            if node in loan:
                if node in agg:
                    x = - (0.5 + agg_loan_iter) * canvas_loan_size / len([x for x in agg if x in loan])
                    y = 0
                    agg_loan_iter += 1
            elif node in non_loan:
                if node in agg:
                    x = (0.5 + agg_nonloan_iter) * canvas_nonloan_size / len([x for x in agg if x in non_loan])
                    y = 0
                    agg_nonloan_iter += 1
        position[node] = (x, y)
    
    # sub-fac 1
    for node in [x for x in agg if x in loan]:
        sub1_loan_iter = 0
        children = [y for y in G.neighbors(node) if y in sub1]
        for child in children:
            x0 = position[node][0]
            x = (x0 + 0.5 * canvas_loan_size_sub1) - (0.5 + sub1_loan_iter) * canvas_loan_size_sub1 / len(children)
            y = - 0.4
            sub1_loan_iter += 1
            position[child] = (x, y)
    
    for node in [x for x in agg if x in non_loan]:
        sub1_nonloan_iter = 0
        children = [y for y in G.neighbors(node) if y in sub1]
        for child in children:
            x0 = position[node][0]
            x = (x0 - 0.5 * canvas_nonloan_size_sub1) + (0.5 + sub1_nonloan_iter) * canvas_nonloan_size_sub1 / len(children)
            y = - 0.4
            sub1_nonloan_iter += 1
            position[child] = (x, y)

    # sub-fac 2
    for node in [x for x in sub1 if x in loan]:
        sub2_loan_iter = 0
        children = [y for y in G.neighbors(node) if y in sub2]
        for child in children:
            x0 = position[node][0]
            x = (x0 + 0.5 * canvas_loan_size_sub2) - (0.5 + sub2_loan_iter) * canvas_loan_size_sub2 / len(children)
            y = - 0.8
            sub2_loan_iter += 1
            position[child] = (x, y)
    
    for node in [x for x in sub1 if x in non_loan]:
        sub2_nonloan_iter = 0
        children = [y for y in G.neighbors(node) if y in sub2]
        for child in children:
            x0 = position[node][0]
            x = (x0 - 0.5 * canvas_nonloan_size_sub2) + (0.5 + sub2_nonloan_iter) * canvas_nonloan_size_sub2 / len(children)
            y = - 0.8
            sub2_nonloan_iter += 1
            position[child] = (x, y)

            # if node in loan:
            #     if node in agg:
            #         x = - (0.5 + agg_loan_iter) * canvas_loan_size / len([x for x in agg if x in loan])
            #         y = 0
            #         agg_loan_iter += 1
            #     elif node in sub1:
            #         x = - (0.5 + sub1_loan_iter) * canvas_loan_size / len([x for x in sub1 if x in loan])
            #         y = -0.4
            #         sub1_loan_iter += 1
            #     elif node in sub2:
            #         x = - (0.5 + sub2_loan_iter) * canvas_loan_size / len([x for x in sub2 if x in loan])
            #         y = -0.8
            #         sub2_loan_iter += 1
            # elif node in non_loan:
            #     if node in agg:
            #         x = (0.5 + agg_nonloan_iter) * canvas_nonloan_size / len([x for x in agg if x in non_loan])
            #         y = 0
            #         agg_nonloan_iter += 1
            #     elif node in sub1:
            #         x = (0.5 + sub1_nonloan_iter) * canvas_nonloan_size / len([x for x in sub1 if x in non_loan])
            #         y = -0.4
            #         sub1_nonloan_iter += 1
            #     elif node in sub2:
            #         x = (0.5 + sub2_nonloan_iter) * canvas_nonloan_size / len([x for x in sub2 if x in non_loan])
            #         y = -0.8
            #         sub2_nonloan_iter += 1
        # position[node] = (x, y)

    return canvas_loan_size, canvas_nonloan_size, position
