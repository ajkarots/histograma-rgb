"""Histogram calculation and visualization utilities."""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from typing import Tuple


class HistogramPlotter:
    """Handles histogram calculation and visualization."""
    
    def __init__(self):
        """Initialize the histogram plotter."""
        # Set matplotlib style
        plt.style.use('default')
    
    def calculate_histogram(self, channel: np.ndarray, bins: int = 256) -> np.ndarray:
        """Calculate histogram for a single channel.
        
        Args:
            channel: Single channel image array
            bins: Number of histogram bins (default 256)
            
        Returns:
            Histogram array
        """
        hist = cv2.calcHist([channel], [0], None, [bins], [0, 256])
        return hist.flatten()
    
    def plot_histograms(self,
                       original: np.ndarray,
                       processed: np.ndarray,
                       channel: int,
                       channel_name: str) -> Tuple[Figure, Figure]:
        """Plot histograms for original and processed images.
        
        Args:
            original: Original image array (BGR format)
            processed: Processed image array (BGR format)
            channel: Channel index (0=Blue, 1=Green, 2=Red in BGR)
            channel_name: Name of channel for title
            
        Returns:
            Tuple of (original_figure, processed_figure)
        """
        # Split channels
        original_split = cv2.split(original)
        processed_split = cv2.split(processed)
        
        orig_channel = original_split[channel]
        proc_channel = processed_split[channel]
        
        # Calculate histograms
        hist_orig = self.calculate_histogram(orig_channel)
        hist_proc = self.calculate_histogram(proc_channel)
        
        # Determine color for plotting
        colors = {0: 'blue', 1: 'green', 2: 'red'}
        color = colors.get(channel, 'gray')
        
        # Plot original
        fig_orig = plt.figure(figsize=(7, 3))
        plt.plot(hist_orig, color=color, linewidth=2)
        plt.fill_between(range(len(hist_orig)), hist_orig, alpha=0.3, color=color)
        plt.title(f'Histograma Original - {channel_name}', fontsize=10, fontweight='bold')
        plt.xlabel('Intensidad (0-255)', fontsize=9)
        plt.ylabel('Cantidad de píxeles', fontsize=9)
        plt.grid(alpha=0.3)
        plt.tight_layout()
        
        # Plot processed
        fig_proc = plt.figure(figsize=(7, 3))
        plt.plot(hist_proc, color=color, linewidth=2)
        plt.fill_between(range(len(hist_proc)), hist_proc, alpha=0.3, color=color)
        plt.title(f'Histograma Procesado - {channel_name}', fontsize=10, fontweight='bold')
        plt.xlabel('Intensidad (0-255)', fontsize=9)
        plt.ylabel('Cantidad de píxeles', fontsize=9)
        plt.grid(alpha=0.3)
        plt.tight_layout()
        
        return fig_orig, fig_proc
    
    def get_stats(self, image: np.ndarray) -> dict:
        """Get statistics for the image.
        
        Args:
            image: Image array (BGR format)
            
        Returns:
            Dictionary with image statistics
        """
        blue, green, red = cv2.split(image)
        
        stats = {
            'red': {'mean': np.mean(red), 'std': np.std(red)},
            'green': {'mean': np.mean(green), 'std': np.std(green)},
            'blue': {'mean': np.mean(blue), 'std': np.std(blue)}
        }
        return stats
