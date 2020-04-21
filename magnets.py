import numpy as np
import matplotlib.pyplot as plt

def magnitude(vector):
    return np.sqrt(np.sum(vector**2))

def magnitude_2d(matrix):
    return np.sqrt(np.sum(np.transpose(matrix, [1,2,0])**2, axis=2))

def mag_field(m_a, p_space_a, p_dipole_a):
    u0 = 1.25663706e-6
    m = np.asarray(m_a)
    p_space = np.asarray(p_space_a)
    p_dipole = np.asarray(p_dipole_a)

    r_vec = p_space - p_dipole 
    r_mag = np.expand_dims(magnitude(r_vec), axis=0)
    r_hat = r_vec/r_mag
    B = (3*(np.dot(m, r_hat)*r_hat - m)) * u0/(4*np.pi*r_mag**3) 
    return B

def expanded_log(matrix):
    signs = np.sign(matrix)
    logs = np.log(np.abs(matrix))
    return logs*signs

class Magnet_Space(object):
    def __init__(self, xs, ys): #takes a numpy array of xs, and numpy array of ys
        self.xs = xs
        self.ys = ys
        self.shape = (xs.shape[0], ys.shape[0])
        I = np.transpose(np.indices(self.shape), [1,2,0])
        self.indices = np.reshape(I, [I.shape[0]*I.shape[1], 2])
        self.magnets = []
        self.recompute_field()

    def add_magnet(self, strength, location): # strength is the dipole moment, vector of length 2. location is the position on the xy plane, vector of length 2.
        self.magnets.append([strength, location])
    
    def recompute_field(self): # call this after adding/subtracting magnets to compute the magnetic field. 
        components = []
        for _ in self.shape:
            components.append(np.zeros(self.shape))
        components = np.asarray(components)

        for magnet in self.magnets:
            strength = magnet[0]
            dipole_location = magnet[1]
            for pt in self.indices:
                field_location = [self.xs[pt[0]], self.ys[pt[1]]]
                B = mag_field(strength, field_location, dipole_location)
                for i, _ in enumerate(self.shape):
                    components[i][tuple(pt)] += B[i]
        
        self.components = components
        self.magnitude = magnitude_2d(self.components)

    def plot_magnitude(self): # plot the magnitude of the magnetic field. doesn't give direction.
        plt.imshow(np.log(self.magnitude), cmap='hot', interpolation='nearest')
        plt.show()

    def plot_nulls(self, detection=2e-9): # plot, where white represents areas where the magnitude of the magnetic field < the detection limit. This might be our graphing function. 
        nones = np.less(self.magnitude, detection)
        plt.imshow(nones, cmap='hot', interpolation='nearest')
        plt.show()

    def plot_field_lines(self, normalized = True): #plot the magnetic field. Not really as nice as you'd expect. Clipped so that there are not really weird looking arrows. Flipped vertically to be consistent with other plots.
        if normalized:
            modified_x = self.components[0]/self.magnitude
            modified_y = self.components[1]/self.magnitude
        else:           
            modified_x = np.clip(self.components[0], -1e-8, 1e-8)
            modified_y = np.clip(self.components[1], -1e-8, 1e-8)
        plt.quiver(range(self.shape[0]), -1*np.asarray(range(self.shape[1])),  modified_x, modified_y)
        plt.show()

    def plot_stream(self): 
        plt.streamplot(np.asarray(range(self.shape[0])), -1*np.asarray(range(self.shape[1])),  self.components[0], self.components[1])
        plt.show()

