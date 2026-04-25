"""Image processing utilities for RGB channel manipulation."""

import cv2
import numpy as np
from typing import Tuple


class ImageProcessor:
    """Handles image loading, processing and manipulation."""
    
    MAX_WIDTH = 600
    
    def __init__(self):
        """Initialize the image processor."""
        pass
    
    def resize_image(self, image: np.ndarray) -> np.ndarray:
        """Resize image to max width while maintaining aspect ratio.
        
        Args:
            image: Input image array (BGR format)
            
        Returns:
            Resized image array
        """
        height, width = image.shape[:2]
        
        if width <= self.MAX_WIDTH:
            return image
        
        # Calculate new height maintaining aspect ratio
        ratio = self.MAX_WIDTH / width
        new_height = int(height * ratio)
        
        resized = cv2.resize(image, (self.MAX_WIDTH, new_height), interpolation=cv2.INTER_AREA)
        return resized
    
    def decompose_rgb(self, image: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Decompose image into RGB channels.
        
        Args:
            image: Input image array (BGR format from OpenCV)
            
        Returns:
            Tuple of (Red, Green, Blue) channel arrays
        """
        # OpenCV uses BGR, so we need to split accordingly
        blue, green, red = cv2.split(image)
        return red, green, blue
    
    def apply_saturation(self,
                        image: np.ndarray,
                        red_factor: float,
                        green_factor: float,
                        blue_factor: float) -> np.ndarray:
        """Apply saturation factors to RGB channels.
        
        Args:
            image: Input image array (BGR format)
            red_factor: Multiplication factor for red channel (0.0-2.0)
            green_factor: Multiplication factor for green channel (0.0-2.0)
            blue_factor: Multiplication factor for blue channel (0.0-2.0)
            
        Returns:
            Processed image array
        """
        # Split channels
        blue, green, red = cv2.split(image)
        
        # Apply factors with float conversion for accuracy
        red_processed = np.clip(red.astype(np.float32) * red_factor, 0, 255).astype(np.uint8)
        green_processed = np.clip(green.astype(np.float32) * green_factor, 0, 255).astype(np.uint8)
        blue_processed = np.clip(blue.astype(np.float32) * blue_factor, 0, 255).astype(np.uint8)
        
        # Merge channels back
        result = cv2.merge([blue_processed, green_processed, red_processed])
        return result
    
    def to_grayscale(self, image: np.ndarray) -> np.ndarray:
        """Convert image to grayscale using standard weighting.
        
        Args:
            image: Input image array (BGR format)
            
        Returns:
            Grayscale image array
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray
    
    def get_image_stats(self, image: np.ndarray) -> dict:
        """Get statistics for each RGB channel.
        
        Args:
            image: Input image array (BGR format)
            
        Returns:
            Dictionary with mean and std for each channel
        """
        blue, green, red = cv2.split(image)
        
        stats = {
            'red': {
                'mean': np.mean(red),
                'std': np.std(red),
                'min': np.min(red),
                'max': np.max(red)
            },
            'green': {
                'mean': np.mean(green),
                'std': np.std(green),
                'min': np.min(green),
                'max': np.max(green)
            },
            'blue': {
                'mean': np.mean(blue),
                'std': np.std(blue),
                'min': np.min(blue),
                'max': np.max(blue)
            }
        }
        return stats
