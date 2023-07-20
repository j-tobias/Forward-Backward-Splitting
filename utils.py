from ForwardBackward import Objective, GradObjective
import plotly.graph_objects as go
import numpy as np



def plot_objective (samples, steps, M, y, tau):

    if type(steps) == np.ndarray:
        pass
    else:
        steps = samples

    step_results = [Objective(M, step, y, tau) for step in steps]
    results = [Objective(M, sample, y, tau) for sample in samples]
    # Extract X, Z, and Y values for the 3D plot
    X = samples[:, 0]
    Z = samples[:, 1]
    Y = results

    # Extract X, Z, and Y values for the second set of samples
    X_steps = steps[:, 0]
    Z_steps = steps[:, 1]
    Y_steps = step_results

    # Create a 3D scatter plot using Plotly
    fig = go.Figure()

    # Scatter plot of the original samples (X, Z, Y) in blue
    fig.add_trace(go.Scatter3d(x=X, y=Z, z=Y, mode='markers', marker=dict(size=3), name='Samples'))

    # Scatter plot of the second set of samples (X, Z, Y) in red
    fig.add_trace(go.Scatter3d(x=X_steps, y=Z_steps, z=Y_steps, mode='markers', marker=dict(size=2), name='Steps'))

    # Update layout for better visualization
    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Z',
            zaxis_title='Y',
        ),
        title='Function Results for 1000 Samples and Steps',
        height = 1000,
    )

    # Show the 3D plot
    return fig

def plot_objective_and_derivative (samples, M, y, tau):



    obj_results = [Objective(M, sample, y, tau) for sample in samples]
    deriv_results = [GradObjective(M, sample, y, tau) for sample in samples]
    # Extract X, Z, and Y values for the 3D plot
    X = samples[:, 0]
    Z = samples[:, 1]
    Y = deriv_results

    # Extract X, Z, and Y values for the second set of samples
    X_steps = samples[:, 0]
    Z_steps = samples[:, 1]
    Y_steps = obj_results

    # Create a 3D scatter plot using Plotly
    fig = go.Figure()

    # Scatter plot of the original samples (X, Z, Y) in blue
    fig.add_trace(go.Scatter3d(x=X, y=Z, z=Y, mode='markers', marker=dict(size=3), name='Derivative'))

    # Scatter plot of the second set of samples (X, Z, Y) in red
    fig.add_trace(go.Scatter3d(x=X_steps, y=Z_steps, z=Y_steps, mode='markers', marker=dict(size=2), name='Objective'))

    # Update layout for better visualization
    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Z',
            zaxis_title='Y',
        ),
        title='Function Results for 1000 Samples and Steps',
        height = 1000,
    )

    # Show the 3D plot
    return fig