/**
 * EasyTin sprite-forge tool
 * Generates and validates pixel sprites based on Endesga 32 palette.
 */

import fs from 'fs';
import path from 'path';

const PALETTE_PATH = path.resolve(process.cwd(), 'palette.json');

export function loadPalette() {
  const data = fs.readFileSync(PALETTE_PATH, 'utf-8');
  return JSON.parse(data);
}

export function validateSpriteMatrix(matrix, validColors) {
  const errors = [];
  matrix.forEach((row, rowIndex) => {
    for (let colIndex = 0; colIndex < row.length; colIndex++) {
      const char = row[colIndex];
      if (char !== '.' && !validColors.has(char)) {
        errors.push(`Invalid color code '${char}' at row ${rowIndex}, col ${colIndex}`);
      }
    }
  });
  return {
    valid: errors.length === 0,
    errors,
  };
}

console.log('✅ sprite-forge: Toolchain initialized successfully.');
