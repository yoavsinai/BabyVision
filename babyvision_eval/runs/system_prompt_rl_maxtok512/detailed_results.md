# Detailed Evaluation Results: runs/system_prompt_rl_maxtok512

## 📊 Summary Statistics
```text
Overall Average Accuracy: 0.1048 ± 0.0032

Type-wise Average Accuracy:
  Fine-grained Discrimination: 0.0961 ± 0.0077
  Spatial Perception: 0.1282 ± 0.0187
  Visual Pattern Recognition: 0.1569 ± 0.0277
  Visual Tracking: 0.0643 ± 0.0248

Subtype-wise Average Accuracy:
  1Fine-grained Discrimination/2D Pattern Completion: 0.3333 ± 0.0624
  1Fine-grained Discrimination/Count Clusters: 0.0556 ± 0.0000
  1Fine-grained Discrimination/Count Same Patterns: 0.0095 ± 0.0135
  1Fine-grained Discrimination/Find the different: 0.0000 ± 0.0000
  1Fine-grained Discrimination/Find the same: 0.0000 ± 0.0000
  1Fine-grained Discrimination/Find the shadow: 0.1884 ± 0.0739
  1Fine-grained Discrimination/Pattern and Color Completion: 0.1500 ± 0.0707
  1Fine-grained Discrimination/Reconstruction: 0.0238 ± 0.0337
  2Visual Tracking/Connect the lines: 0.0526 ± 0.0430
  2Visual Tracking/Lines Observation: 0.0000 ± 0.0000
  2Visual Tracking/Maze: 0.1000 ± 0.0707
  2Visual Tracking/Metro map: 0.0278 ± 0.0393
  2Visual Tracking/Recognize numbers and letters: 0.0870 ± 0.0615
  3Spatial Perception/3D Cube Unfold: 0.0278 ± 0.0393
  3Spatial Perception/3D Pattern Completion: 0.3704 ± 0.0944
  3Spatial Perception/3D Views: 0.0864 ± 0.0462
  3Spatial Perception/Count 3D blocks: 0.0606 ± 0.0429
  3Spatial Perception/Paper Folding: 0.0833 ± 0.0680
  4Visual Pattern Recognition/Logic Patterns: 0.0476 ± 0.0673
  4Visual Pattern Recognition/Mirroring Patterns: 0.2000 ± 0.0816
  4Visual Pattern Recognition/Overlay Patterns: 0.1569 ± 0.0277
  4Visual Pattern Recognition/Rotation Patterns: 0.2667 ± 0.0471
```

## 📝 Detailed Task-wise Results
Total evaluated tasks: **388**

| Task ID | Type / Subtype | Ground Truth | Pass 1 Ans (Judge) | Pass 2 Ans (Judge) | Pass 3 Ans (Judge) | Accuracy |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 445 | Fine-grained Discrimination / Find the different | (4,7) | `(5, 4)` (❌) | `(1,2)` (❌) | `(1,6)` (❌) | **0.0%** |
| 464 | Fine-grained Discrimination / Find the different | (5,9) | `(10, 4)` (❌) | `N/A` (❌) | `(5, 10)` (❌) | **0.0%** |
| 507 | Fine-grained Discrimination / Find the different | (5,7) | `(4,8)` (❌) | `(4, 7)` (❌) | `(4, 7)` (❌) | **0.0%** |
| 525 | Fine-grained Discrimination / Find the different | (7,8) | `(1,1)` (❌) | `(1,1)` (❌) | `(1,1)` (❌) | **0.0%** |
| 534 | Fine-grained Discrimination / Find the different | (6,12) | `(4, 8)` (❌) | `N/A` (❌) | `(4, 11)` (❌) | **0.0%** |
| 638 | Fine-grained Discrimination / Find the different | Row 4 Column 17 | `Row 18 Column 18` (❌) | `8 16` (❌) | `Row 2 Column 18` (❌) | **0.0%** |
| 779 | Fine-grained Discrimination / Find the different | (10, 9) | `(5, 5)` (❌) | `(12, 7)` (❌) | `(4, 8)` (❌) | **0.0%** |
| 879 | Fine-grained Discrimination / Find the different | 10,5 | `(7,9)` (❌) | `(17,13)` (❌) | `(14,15)` (❌) | **0.0%** |
| 910 | Fine-grained Discrimination / Find the different | 9,5 | `2,2` (❌) | `3,5` (❌) | `No face is different` (❌) | **0.0%** |
| 984 | Fine-grained Discrimination / Find the different | (6,10) | `(5,10)` (❌) | `(5, 10)` (❌) | `(5,10)` (❌) | **0.0%** |
| 986 | Fine-grained Discrimination / Find the different | (11,4) | `\text{No such row exists}` (❌) | `N/A` (❌) | `(1,1)` (❌) | **0.0%** |
| 988 | Fine-grained Discrimination / Find the different | (9,7) | `N/A` (❌) | `(14,10)` (❌) | `(9, 9)` (❌) | **0.0%** |
| 4152 | Fine-grained Discrimination / Find the different | (7,2) | `N/A` (❌) | `(7,3)` (❌) | `N/A` (❌) | **0.0%** |
| 6161 | Fine-grained Discrimination / Find the different | (7,8) | `(8,7)` (❌) | `(2, 2)` (❌) | `(7, 13)` (❌) | **0.0%** |
| 6164 | Fine-grained Discrimination / Find the different | (9,2) | `(8, 6)` (❌) | `N/A` (❌) | `(9,1)` (❌) | **0.0%** |
| 6165 | Fine-grained Discrimination / Find the different | 6-7 | `No different silhouette found` (❌) | `11-6` (❌) | `2-3` (❌) | **0.0%** |
| 437 | Fine-grained Discrimination / Find the same | 1-7,2-9,3-10,4-8,6-11 | `1-8` (❌) | `No pairs` (❌) | `3-4, 6-7` (❌) | **0.0%** |
| 462 | Fine-grained Discrimination / Find the same | D | `A` (❌) | `B` (❌) | `C` (❌) | **0.0%** |
| 469 | Fine-grained Discrimination / Find the same | 2-7 | `1-4` (❌) | `1-4` (❌) | `1-4` (❌) | **0.0%** |
| 475 | Fine-grained Discrimination / Find the same | (1,3)-(3,1) | `(1,1)-(3,1)` (❌) | `(3,1)-(3,2)` (❌) | `N/A` (❌) | **0.0%** |
| 476 | Fine-grained Discrimination / Find the same | 4-11 | `3-14` (❌) | `2-4` (❌) | `2-3` (❌) | **0.0%** |
| 478 | Fine-grained Discrimination / Find the same | 2,3,6,7,10 | `2,3,4,5,6,7,8,9,10` (❌) | `2,3,4,5,6,7,8,9,10` (❌) | `2,3` (❌) | **0.0%** |
| 498 | Fine-grained Discrimination / Find the same | BG,CE,DF | `N/A` (❌) | `AB,CD,EF` (❌) | `AD,BE,CF` (❌) | **0.0%** |
| 522 | Fine-grained Discrimination / Find the same | E | `B` (❌) | `A` (❌) | `N/A` (❌) | **0.0%** |
| 617 | Fine-grained Discrimination / Find the same | C | `A` (❌) | `A` (❌) | `B` (❌) | **0.0%** |
| 626 | Fine-grained Discrimination / Find the same | Second row third column | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 635 | Fine-grained Discrimination / Find the same | 9-12 | `No pairs` (❌) | `No pairs` (❌) | `1-2, 3-4, 5-6, 7-8, 9-10, 11-12, 13-14` (❌) | **0.0%** |
| 651 | Fine-grained Discrimination / Find the same | 4-11 | `No pairs` (❌) | `N/A` (❌) | `1-2` (❌) | **0.0%** |
| 711 | Fine-grained Discrimination / Find the same | (2-1)-(3-3) | `(2-1)-(3-2)` (❌) | `(1-1)-(2-1)` (❌) | `(1-1)-(2-1)` (❌) | **0.0%** |
| 720 | Fine-grained Discrimination / Find the same | 12 | `N/A` (❌) | `1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25` (❌) | `N/A` (❌) | **0.0%** |
| 4698 | Fine-grained Discrimination / Find the same | 2D,6A,4B,1B,5C,1F | `N/A` (❌) | `N/A` (❌) | `1A, 2B, 3C, 4D, 5E, 6F` (❌) | **0.0%** |
| 5597 | Fine-grained Discrimination / Find the same | 2,4,5,6,7,9 | `N/A` (❌) | `5,6` (❌) | `2,3,4,5,6,7,8,9,10` (❌) | **0.0%** |
| 7568 | Fine-grained Discrimination / Find the same | F | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 459 | Fine-grained Discrimination / Find the shadow | 1-4,3-12,5-10,7-2,9-6,11-8 | `1-2,3-4,5-6,7-8,9-10,11-12` (❌) | `N/A` (❌) | `1-2,3-4,5-6,7-8,9-10,11-12` (❌) | **0.0%** |
| 644 | Fine-grained Discrimination / Find the shadow | 1-6,2-5,3-8,4-11,5-12,6-7 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 826 | Fine-grained Discrimination / Find the shadow | 1-6,3-4,5-8,7-12,9-10,11-2 | `N/A` (❌) | `1-2, 3-4, 5-6, 7-8, 9-10, 11-12` (❌) | `1-4, 3-6, 5-2, 7-8, 9-10, 11-12` (❌) | **0.0%** |
| 4994 | Fine-grained Discrimination / Find the shadow | D | `B` (❌) | `C` (❌) | `D` (✅) | **33.3%** |
| 4996 | Fine-grained Discrimination / Find the shadow | C | `C` (✅) | `C` (✅) | `C` (✅) | **100.0%** |
| 4998 | Fine-grained Discrimination / Find the shadow | B | `C` (❌) | `D` (❌) | `B` (✅) | **33.3%** |
| 5001 | Fine-grained Discrimination / Find the shadow | Second row third column | `1, 1` (❌) | `2, 1` (❌) | `1, 1` (❌) | **0.0%** |
| 5004 | Fine-grained Discrimination / Find the shadow | Second row first column | `2, 3` (❌) | `Row 2, Column 3` (❌) | `2, 2` (✅) | **33.3%** |
| 5006 | Fine-grained Discrimination / Find the shadow | Row 1, Column 2 | `Row 1, Column 1` (❌) | `Row 1, Column 2` (✅) | `Row 2, Column 2` (❌) | **33.3%** |
| 5008 | Fine-grained Discrimination / Find the shadow | The second row, third column | `2, 2` (❌) | `Row 1, Column 1` (❌) | `(3, 2)` (✅) | **33.3%** |
| 5009 | Fine-grained Discrimination / Find the shadow | Row 1 Column 3 | `1, 2` (❌) | `3, 3` (❌) | `1, 1` (❌) | **0.0%** |
| 5011 | Fine-grained Discrimination / Find the shadow | Third row first column | `Row 2, Column 2` (❌) | `Row 1, Column 2` (❌) | `Row 2, Column 3` (❌) | **0.0%** |
| 5013 | Fine-grained Discrimination / Find the shadow | Third Row Second Column | `2, 1` (✅) | `2 2` (✅) | `2, 1` (✅) | **100.0%** |
| 5016 | Fine-grained Discrimination / Find the shadow | 1-C,2-G,3-D,4-E,5-B,6-F,7-A | `1-C, 2-B, 3-A, 4-D, 5-E, 6-F, 7-G` (❌) | `1-C, 2-B, 3-A, 4-D, 5-E, 6-F, 7-G` (❌) | `1-C, 2-B, 3-D, 4-A, 5-E, 6-F, 7-G` (❌) | **0.0%** |
| 5018 | Fine-grained Discrimination / Find the shadow | The third row and first column | `Row 1, Column 1` (❌) | `Row 1, Column 2` (❌) | `Row 1, Column 1` (❌) | **0.0%** |
| 5020 | Fine-grained Discrimination / Find the shadow | Second column, first one | `(3, 3)` (❌) | `3, 3` (❌) | `(3, 1)` (❌) | **0.0%** |
| 5022 | Fine-grained Discrimination / Find the shadow | The first row and second column | `Bottom-left` (❌) | `1, 2` (✅) | `(3, 1)` (❌) | **33.3%** |
| 5023 | Fine-grained Discrimination / Find the shadow | Second row second | `Row 3, Column 3` (❌) | `3,2` (✅) | `(4, 3)` (❌) | **33.3%** |
| 5025 | Fine-grained Discrimination / Find the shadow | 1-G,2-D,3-A,4-F,6-B,7-E,8-H,9-C | `1-A, 2-B, 3-C, 4-D, 9-E, 6-F, 7-G, 8-H` (❌) | `N/A` (❌) | `1-A, 2-B, 3-C, 4-D, 9-E, 6-F, 7-G, 8-H` (❌) | **0.0%** |
| 5026 | Fine-grained Discrimination / Find the shadow | 1-F,2-D,3-E,4-B,6-H,7-A,8-G,9-C | `1-E, 2-B, 3-C, 4-D, 6-H, 7-F, 8-G, 9-A` (❌) | `N/A` (❌) | `1-E, 2-B, 3-C, 4-D, 6-H, 7-F, 8-G, 9-A` (❌) | **0.0%** |
| 5030 | Fine-grained Discrimination / Find the shadow | 1-F,2-G,3-D,4-B,6-C,7-H,8-A,9-E | `1-C, 2-D, 3-A, 4-B, 6-E, 7-F, 8-G, 9-H` (❌) | `1-E, 2-A, 3-C, 4-F, 6-B, 7-G, 8-D, 9-H` (❌) | `1-F, 2-C, 3-E, 4-B, 6-A, 7-G, 8-D, 9-H` (❌) | **0.0%** |
| 6504 | Fine-grained Discrimination / Find the shadow | 1-4,2-3,3-1,4-2 | `1-4, 2-3, 3-2, 4-1` (❌) | `1-1, 2-2, 3-3, 4-4` (❌) | `N/A` (❌) | **0.0%** |
| 6512 | Fine-grained Discrimination / Find the shadow | 1-7,2-8,3-6,4-10,5-9 | `N/A` (❌) | `1-7,2-8,3-9,4-6,5-10` (❌) | `1-6,2-7,3-8,4-9,5-10` (❌) | **0.0%** |
| 535 | Fine-grained Discrimination / Reconstruction | B | `C` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 2353 | Fine-grained Discrimination / Reconstruction | C | `A` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 5270 | Fine-grained Discrimination / Reconstruction | 2,3,5 | `1, 2, 3, 4` (❌) | `1,2,3,4` (❌) | `3, 5` (❌) | **0.0%** |
| 5271 | Fine-grained Discrimination / Reconstruction | 1,3,4 | `1, 4` (❌) | `1, 2, 3, 4` (❌) | `1,2,3,4` (❌) | **0.0%** |
| 5274 | Fine-grained Discrimination / Reconstruction | 1,3,4,5 | `1,2,3,4` (❌) | `1, 2, 3, 4, 5` (❌) | `1, 2, 3, 4` (❌) | **0.0%** |
| 5275 | Fine-grained Discrimination / Reconstruction | 2,3,4,5 | `1,2,3,5` (❌) | `1, 2, 5` (❌) | `N/A` (❌) | **0.0%** |
| 5276 | Fine-grained Discrimination / Reconstruction | 1,3,4,6,8 | `1, 3, 4` (❌) | `1,3,4,7` (❌) | `3, 5` (❌) | **0.0%** |
| 5277 | Fine-grained Discrimination / Reconstruction | 1,2,4,5,8 | `1, 3, 4, 6` (❌) | `1, 3, 4, 5` (❌) | `1, 2, 5, 6` (❌) | **0.0%** |
| 5339 | Fine-grained Discrimination / Reconstruction | 1-9, 2-8, 3-10, 4-6, 5-7 | `1-9, 2-8, 3-10, 4-6, 5-7` (✅) | `N/A` (❌) | `N/A` (❌) | **33.3%** |
| 6131 | Fine-grained Discrimination / Reconstruction | 1-B,2-C,3-D,4-A | `1-A, 2-B, 3-C, 4-D` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | **0.0%** |
| 6134 | Fine-grained Discrimination / Reconstruction | 1-B,2-D,3-A,4-C | `1-A, 2-B, 3-C, 4-D` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | **0.0%** |
| 6136 | Fine-grained Discrimination / Reconstruction | 1-C,2-D,3-A,4-B | `1-A, 2-B, 3-C, 4-D` (❌) | `N/A` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | **0.0%** |
| 6137 | Fine-grained Discrimination / Reconstruction | 1-D,2-A,3-B,4-C | `1-A, 2-B, 3-C, 4-D` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | **0.0%** |
| 6273 | Fine-grained Discrimination / Reconstruction | A-6, B-3, C-4, D-1, E-2, F-5 | `N/A` (❌) | `N/A` (❌) | `B-1, A-2, D-3, C-4, F-5, E-6` (❌) | **0.0%** |
| 457 | Fine-grained Discrimination / 2D Pattern Completion | C | `C` (✅) | `B` (❌) | `C` (✅) | **66.7%** |
| 494 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 637 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 640 | Fine-grained Discrimination / 2D Pattern Completion | A | `A` (✅) | `B` (❌) | `Choice (C)` (❌) | **33.3%** |
| 673 | Fine-grained Discrimination / 2D Pattern Completion | A | `A` (✅) | `A` (✅) | `B` (❌) | **66.7%** |
| 765 | Fine-grained Discrimination / 2D Pattern Completion | A | `A` (✅) | `B` (❌) | `A` (✅) | **66.7%** |
| 876 | Fine-grained Discrimination / 2D Pattern Completion | B | `C` (❌) | `B` (✅) | `B` (✅) | **66.7%** |
| 3995 | Fine-grained Discrimination / 2D Pattern Completion | C | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 4026 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `B` (❌) | `A` (✅) | **33.3%** |
| 4104 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `N/A` (❌) | `B` (❌) | **0.0%** |
| 4133 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `C` (❌) | `D` (❌) | **0.0%** |
| 4142 | Fine-grained Discrimination / 2D Pattern Completion | C | `D` (❌) | `D` (❌) | `B` (❌) | **0.0%** |
| 4173 | Fine-grained Discrimination / 2D Pattern Completion | C | `B` (❌) | `A` (❌) | `N/A` (❌) | **0.0%** |
| 4188 | Fine-grained Discrimination / 2D Pattern Completion | A | `A` (✅) | `A` (✅) | `A` (✅) | **100.0%** |
| 4190 | Fine-grained Discrimination / 2D Pattern Completion | B | `B` (✅) | `C` (❌) | `B` (✅) | **66.7%** |
| 4386 | Fine-grained Discrimination / 2D Pattern Completion | A | `A` (✅) | `A` (✅) | `B` (❌) | **66.7%** |
| 4399 | Fine-grained Discrimination / 2D Pattern Completion | A | `A` (✅) | `A` (✅) | `A` (✅) | **100.0%** |
| 4405 | Fine-grained Discrimination / 2D Pattern Completion | D | `B` (❌) | `(B)` (❌) | `B` (❌) | **0.0%** |
| 4415 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 4712 | Fine-grained Discrimination / 2D Pattern Completion | C | `B)` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 559 | Fine-grained Discrimination / Pattern and Color Completion | A | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 628 | Fine-grained Discrimination / Pattern and Color Completion | C | `N/A` (❌) | `C` (✅) | `B` (❌) | **33.3%** |
| 633 | Fine-grained Discrimination / Pattern and Color Completion | B | `Choice (B)` (✅) | `Answer: (B)` (✅) | `Choice (B)` (✅) | **100.0%** |
| 639 | Fine-grained Discrimination / Pattern and Color Completion | C | `A` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 645 | Fine-grained Discrimination / Pattern and Color Completion | A | `B` (❌) | `A` (✅) | `B` (❌) | **33.3%** |
| 652 | Fine-grained Discrimination / Pattern and Color Completion | C | `A` (❌) | `N/A` (❌) | `C` (✅) | **33.3%** |
| 695 | Fine-grained Discrimination / Pattern and Color Completion | C | `A` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 699 | Fine-grained Discrimination / Pattern and Color Completion | D | `B` (❌) | `C` (❌) | `B` (❌) | **0.0%** |
| 721 | Fine-grained Discrimination / Pattern and Color Completion | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 790 | Fine-grained Discrimination / Pattern and Color Completion | D | `A` (❌) | `N/A` (❌) | `A` (❌) | **0.0%** |
| 792 | Fine-grained Discrimination / Pattern and Color Completion | C | `D` (❌) | `N/A` (❌) | `A` (❌) | **0.0%** |
| 1594 | Fine-grained Discrimination / Pattern and Color Completion | B | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 4146 | Fine-grained Discrimination / Pattern and Color Completion | C | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 4148 | Fine-grained Discrimination / Pattern and Color Completion | C | `A` (❌) | `C` (✅) | `A` (❌) | **33.3%** |
| 4181 | Fine-grained Discrimination / Pattern and Color Completion | B | `A` (❌) | `C` (❌) | `D` (❌) | **0.0%** |
| 4768 | Fine-grained Discrimination / Pattern and Color Completion | 1-D,2-B,3-A,4-C | `N/A` (❌) | `N/A` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | **0.0%** |
| 5123 | Fine-grained Discrimination / Pattern and Color Completion | Row 2, Column 3 | `2, 2` (❌) | `2, 2` (❌) | `N/A` (❌) | **0.0%** |
| 5399 | Fine-grained Discrimination / Pattern and Color Completion | B | `B` (✅) | `B` (✅) | `C` (❌) | **66.7%** |
| 6206 | Fine-grained Discrimination / Pattern and Color Completion | 2,6,8 | `1,5,9` (❌) | `1,5,9` (❌) | `1,5,7` (❌) | **0.0%** |
| 7858 | Fine-grained Discrimination / Pattern and Color Completion | B | `A` (❌) | `A` (❌) | `N/A` (❌) | **0.0%** |
| 4534 | Fine-grained Discrimination / Count Same Patterns | 14 | `10` (❌) | `13` (❌) | `10` (❌) | **0.0%** |
| 4536 | Fine-grained Discrimination / Count Same Patterns | 15 | `5` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 4537 | Fine-grained Discrimination / Count Same Patterns | 13 | `N/A` (❌) | `10` (❌) | `7` (❌) | **0.0%** |
| 4540 | Fine-grained Discrimination / Count Same Patterns | 18 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 4552 | Fine-grained Discrimination / Count Same Patterns | 54 | `57` (❌) | `36` (❌) | `38` (❌) | **0.0%** |
| 4553 | Fine-grained Discrimination / Count Same Patterns | 58 | `42` (❌) | `30` (❌) | `30` (❌) | **0.0%** |
| 4554 | Fine-grained Discrimination / Count Same Patterns | 42 | `24` (❌) | `N/A` (❌) | `31` (❌) | **0.0%** |
| 4556 | Fine-grained Discrimination / Count Same Patterns | 67 | `52` (❌) | `42` (❌) | `56` (❌) | **0.0%** |
| 4558 | Fine-grained Discrimination / Count Same Patterns | 54 | `51` (❌) | `27` (❌) | `44` (❌) | **0.0%** |
| 4560 | Fine-grained Discrimination / Count Same Patterns | 36 | `22` (❌) | `11` (❌) | `16` (❌) | **0.0%** |
| 4561 | Fine-grained Discrimination / Count Same Patterns | 38 | `33` (❌) | `26` (❌) | `24` (❌) | **0.0%** |
| 4562 | Fine-grained Discrimination / Count Same Patterns | 36 | `20` (❌) | `16` (❌) | `17` (❌) | **0.0%** |
| 4564 | Fine-grained Discrimination / Count Same Patterns | 32 | `22` (❌) | `21` (❌) | `14` (❌) | **0.0%** |
| 4566 | Fine-grained Discrimination / Count Same Patterns | 17 | `11` (❌) | `9` (❌) | `10` (❌) | **0.0%** |
| 4568 | Fine-grained Discrimination / Count Same Patterns | 34 | `24` (❌) | `N/A` (❌) | `18` (❌) | **0.0%** |
| 4571 | Fine-grained Discrimination / Count Same Patterns | 36 | `15` (❌) | `15` (❌) | `14` (❌) | **0.0%** |
| 5073 | Fine-grained Discrimination / Count Same Patterns | 23 | `32` (❌) | `15` (❌) | `3` (❌) | **0.0%** |
| 5074 | Fine-grained Discrimination / Count Same Patterns | 22 | `N/A` (❌) | `N/A` (❌) | `5` (❌) | **0.0%** |
| 5081 | Fine-grained Discrimination / Count Same Patterns | 18 | `12` (❌) | `12` (❌) | `N/A` (❌) | **0.0%** |
| 5082 | Fine-grained Discrimination / Count Same Patterns | 14 | `23` (❌) | `18` (❌) | `14` (✅) | **33.3%** |
| 5083 | Fine-grained Discrimination / Count Same Patterns | 24 | `N/A` (❌) | `N/A` (❌) | `12` (❌) | **0.0%** |
| 5084 | Fine-grained Discrimination / Count Same Patterns | 24 | `N/A` (❌) | `18` (❌) | `18` (❌) | **0.0%** |
| 5085 | Fine-grained Discrimination / Count Same Patterns | 18 | `16` (❌) | `32` (❌) | `16` (❌) | **0.0%** |
| 5086 | Fine-grained Discrimination / Count Same Patterns | 34 | `N/A` (❌) | `25` (❌) | `8` (❌) | **0.0%** |
| 5357 | Fine-grained Discrimination / Count Same Patterns | 8, 3, 7, 4, 5, 6 | `12,0,11,9,7,3` (❌) | `N/A` (❌) | `9,0,10,11,6,0` (❌) | **0.0%** |
| 5358 | Fine-grained Discrimination / Count Same Patterns | 7, 4, 5, 9, 2 | `12,11,10,11,5` (❌) | `21,13,14,14,8` (❌) | `9,8,7,8,1` (❌) | **0.0%** |
| 5638 | Fine-grained Discrimination / Count Same Patterns | 4 | `1` (❌) | `1` (❌) | `0` (❌) | **0.0%** |
| 5639 | Fine-grained Discrimination / Count Same Patterns | 4 | `N/A` (❌) | `0` (❌) | `3` (❌) | **0.0%** |
| 5640 | Fine-grained Discrimination / Count Same Patterns | 5 | `15` (❌) | `17` (❌) | `15` (❌) | **0.0%** |
| 5781 | Fine-grained Discrimination / Count Same Patterns | 5 | `18` (❌) | `16` (❌) | `N/A` (❌) | **0.0%** |
| 5786 | Fine-grained Discrimination / Count Same Patterns | 10 | `0` (❌) | `6` (❌) | `3` (❌) | **0.0%** |
| 6421 | Fine-grained Discrimination / Count Same Patterns | 7,6,2,7,9,5 | `6,4,3,5,8,2` (❌) | `13, 7, 3, 6, 0, 0` (❌) | `7,6,3,6,5,2` (❌) | **0.0%** |
| 6436 | Fine-grained Discrimination / Count Same Patterns | 8,7,3,2 | `N/A` (❌) | `4,4,4,4` (❌) | `4,4,4,4` (❌) | **0.0%** |
| 6466 | Fine-grained Discrimination / Count Same Patterns | 5,6,5,8 | `N/A` (❌) | `4,5,5,5` (❌) | `5,5,6,4` (❌) | **0.0%** |
| 6475 | Fine-grained Discrimination / Count Same Patterns | 15,10,11,15 | `5,4,8,8` (❌) | `9,4,5,7` (❌) | `7,6,8,8` (❌) | **0.0%** |
| 496 | Fine-grained Discrimination / Count Clusters | 18 | `9` (❌) | `9` (❌) | `23` (❌) | **0.0%** |
| 4650 | Fine-grained Discrimination / Count Clusters | 19 | `27` (❌) | `24` (❌) | `17` (❌) | **0.0%** |
| 4652 | Fine-grained Discrimination / Count Clusters | 21 | `24` (❌) | `24` (❌) | `23` (❌) | **0.0%** |
| 4653 | Fine-grained Discrimination / Count Clusters | 9 | `6` (❌) | `8` (❌) | `4` (❌) | **0.0%** |
| 5107 | Fine-grained Discrimination / Count Clusters | 8 | `11` (❌) | `13` (❌) | `12` (❌) | **0.0%** |
| 5113 | Fine-grained Discrimination / Count Clusters | 10 | `12` (❌) | `13` (❌) | `13` (❌) | **0.0%** |
| 5114 | Fine-grained Discrimination / Count Clusters | 9 | `12` (❌) | `10` (❌) | `13` (❌) | **0.0%** |
| 5117 | Fine-grained Discrimination / Count Clusters | 8,7 | `13, 4` (❌) | `7,6` (❌) | `9, 3` (❌) | **0.0%** |
| 5119 | Fine-grained Discrimination / Count Clusters | 10 | `11` (❌) | `12` (❌) | `9` (❌) | **0.0%** |
| 5378 | Fine-grained Discrimination / Count Clusters | 6,3,5,5 | `3,4,4,4` (❌) | `5,4,5,5` (❌) | `N/A` (❌) | **0.0%** |
| 5455 | Fine-grained Discrimination / Count Clusters | 2+6+1+3=12 | `2+4+1+3=10` (❌) | `2+6+1+3=12` (✅) | `2+6+1+4=13` (❌) | **33.3%** |
| 5490 | Fine-grained Discrimination / Count Clusters | 8−5=3 | `6-4=2` (❌) | `5-4=1` (❌) | `5-3=2` (❌) | **0.0%** |
| 5492 | Fine-grained Discrimination / Count Clusters | 7−1=6 | `6-1=5` (❌) | `6-1=5` (❌) | `5-2=3` (❌) | **0.0%** |
| 5795 | Fine-grained Discrimination / Count Clusters | 10,14,12 | `29` (❌) | `5, 11, 9` (❌) | `N/A` (❌) | **0.0%** |
| 6534 | Fine-grained Discrimination / Count Clusters | 1-2, 2-1, 3-4, 4-3 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6555 | Fine-grained Discrimination / Count Clusters | > | `=` (❌) | `=` (❌) | `<` (❌) | **0.0%** |
| 6556 | Fine-grained Discrimination / Count Clusters | < | `<` (✅) | `>` (❌) | `<` (✅) | **66.7%** |
| 6557 | Fine-grained Discrimination / Count Clusters | = | `<` (❌) | `<` (❌) | `<` (❌) | **0.0%** |
| 666 | Visual Tracking / Maze | B | `B` (✅) | `Answer: (C)` (❌) | `A` (❌) | **33.3%** |
| 674 | Visual Tracking / Maze | E | `D` (❌) | `A` (❌) | `Yes, the maze appears to have connected paths between the marked points.` (❌) | **0.0%** |
| 817 | Visual Tracking / Maze | A | `C` (❌) | `B` (❌) | `C` (❌) | **0.0%** |
| 980 | Visual Tracking / Maze | C | `A` (❌) | `N/A` (❌) | `C` (✅) | **33.3%** |
| 982 | Visual Tracking / Maze | A | ` (A) ` (✅) | `B` (❌) | `B` (❌) | **33.3%** |
| 983 | Visual Tracking / Maze | A | `B` (❌) | `B` (❌) | `(B)` (❌) | **0.0%** |
| 1306 | Visual Tracking / Maze | B | `(B)` (✅) | `A` (❌) | `(A)` (❌) | **33.3%** |
| 1651 | Visual Tracking / Maze | B | `Choice (A)` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 3782 | Visual Tracking / Maze | C | `Answer: (C)` (✅) | `C` (✅) | `N/A` (❌) | **66.7%** |
| 5124 | Visual Tracking / Maze | 39 | `21` (❌) | `29` (❌) | `N/A` (❌) | **0.0%** |
| 5127 | Visual Tracking / Maze | 59 | `36` (❌) | `35` (❌) | `N/A` (❌) | **0.0%** |
| 5128 | Visual Tracking / Maze | 50 | `N/A` (❌) | `17` (❌) | `N/A` (❌) | **0.0%** |
| 5130 | Visual Tracking / Maze | 57 | `18` (❌) | `11` (❌) | `17` (❌) | **0.0%** |
| 5131 | Visual Tracking / Maze | 53 | `13` (❌) | `10` (❌) | `17` (❌) | **0.0%** |
| 5133 | Visual Tracking / Maze | 51 | `16` (❌) | `N/A` (❌) | `33` (❌) | **0.0%** |
| 5136 | Visual Tracking / Maze | 27 | `N/A` (❌) | `13` (❌) | `15` (❌) | **0.0%** |
| 5139 | Visual Tracking / Maze | 38 | `8` (❌) | `9` (❌) | `12` (❌) | **0.0%** |
| 5140 | Visual Tracking / Maze | 52 | `28` (❌) | `17` (❌) | `13` (❌) | **0.0%** |
| 5142 | Visual Tracking / Maze | 52 | `25` (❌) | `N/A` (❌) | `13` (❌) | **0.0%** |
| 5143 | Visual Tracking / Maze | 55 | `27` (❌) | `29` (❌) | `28` (❌) | **0.0%** |
| 770 | Visual Tracking / Connect the lines | A-2,B-3,C-1 | `A-1, B-2, C-3` (❌) | `A-1, B-3, C-2` (❌) | `A-1, B-2, C-3` (❌) | **0.0%** |
| 1662 | Visual Tracking / Connect the lines | 4,2,6,5,7,3,1 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 2492 | Visual Tracking / Connect the lines | D | `A` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 4327 | Visual Tracking / Connect the lines | 1-B,2-A,3-C | `1-A, 2-B, 3-C` (❌) | `1-A, 2-B, 3-C` (❌) | `1-A, 2-B, 3-C` (❌) | **0.0%** |
| 4329 | Visual Tracking / Connect the lines | 10,7,7 | `5, 7, 6` (❌) | `3, 10, 15` (❌) | `1, 7, 14` (❌) | **0.0%** |
| 4330 | Visual Tracking / Connect the lines | A - Blue, B - Yellow, C - Green | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 4332 | Visual Tracking / Connect the lines | 3-Gem,1-Fan,2-Crab,4-Skull | `a-gem,b-fan,c-crab,d-skull` (❌) | `1-gem,2-fan,3-crab,4-skull` (❌) | `a-gem,b-fan,c-crab,d-skull` (❌) | **0.0%** |
| 4337 | Visual Tracking / Connect the lines | 1-Skull #3, 2-Skull #2, 3-Diamond, 4-Skull #1 | `Line 1 connects to Skull #1, Line 2 connects to the Diamond, Line 3 connects to Skull #2, and Line 4 connects to Skull #3.` (❌) | `Line 1: Skull #1, Line 2: Diamond, Line 3: Skull #2, Line 4: Skull #3` (❌) | `Line 1 to Skull #1, Line 2 to Diamond, Line 3 to Skull #2, Line 4 to Skull #3` (❌) | **0.0%** |
| 4352 | Visual Tracking / Connect the lines | A-Circle, B-Triangle, C-Rectangle, D-Square, E-Pentagram | `A-square, B-circle, C-star, D-triangle, E-rectangle` (❌) | `A-square, B-circle, C-pentagram, D-triangle, E-rectangle` (❌) | `A-square, B-circle, C-pentagram, D-triangle, E-rectangle` (✅) | **33.3%** |
| 5152 | Visual Tracking / Connect the lines | 1-S,2-N,3-O,4-W,5-M,6-A,7-N | `1-W, 2-N, 3-N, 4-O, 5-A, 6-M, 7-S` (❌) | `1-W, 2-N, 3-N, 4-O, 5-A, 6-M, 7-S` (❌) | `1-W,2-N,3-N,4-O,5-A,6-M,7-S` (❌) | **0.0%** |
| 5154 | Visual Tracking / Connect the lines | A-X,B-Y,C-Z,D-W | `A-W,B-X,C-Y,D-Z` (❌) | `A-W, B-X, C-Y, D-Z` (✅) | `A-W, B-X, C-Y, D-Z` (✅) | **66.7%** |
| 5156 | Visual Tracking / Connect the lines | 1-D,2-I,3-A,4-M,5-O,6-N,7-D | `1-A,2-N,3-D,4-D,5-O,6-I,7-M` (❌) | `1-A, 2-N, 3-D, 4-D, 5-O, 6-I, 7-M` (❌) | `1-A, 2-N, 3-D, 4-D, 5-O, 6-I, 7-M` (❌) | **0.0%** |
| 5161 | Visual Tracking / Connect the lines | 1-U,2-M,3-B,4-R,5-E,6-L,7-L,8-A | `1-B,2-L,3-R,4-U,5-A,6-L,7-E,8-M` (❌) | `1-B,2-L,3-R,4-U,5-A,6-L,7-E,8-M` (❌) | `1-B, 2-L, 3-R, 4-U, 5-A, 6-L, 7-E, 8-M` (❌) | **0.0%** |
| 5164 | Visual Tracking / Connect the lines | 1-H,2-E,3-D,4-G,5-E,6-H,7-O,8-G | `1-E,2-H,3-O,4-E,5-G,6-G,7-H,8-D` (❌) | `1-E,2-H,3-O,4-E,5-G,6-G,7-H,8-D` (❌) | `1-E, 2-H, 3-O, 4-E, 5-G, 6-G, 7-H, 8-D` (❌) | **0.0%** |
| 5245 | Visual Tracking / Connect the lines | Still,waters,run,deep | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5246 | Visual Tracking / Connect the lines | Better,late,than,never | `bat, bet, bran, beat` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5247 | Visual Tracking / Connect the lines | Which,witch,is,which | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5248 | Visual Tracking / Connect the lines | Rolling,red,wagons | `N/A` (❌) | `N/A` (❌) | `ROG, RAN, RED` (❌) | **0.0%** |
| 5249 | Visual Tracking / Connect the lines | Daddy,draws,doors | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 447 | Visual Tracking / Recognize numbers and letters | 2,N,Z,S | `N,S,Z,S` (❌) | `yellow, green, blue, red` (❌) | `A,N,Z,S` (❌) | **0.0%** |
| 520 | Visual Tracking / Recognize numbers and letters | G,4,D,6 | `0,4,D,6` (❌) | `O,4,D,6` (❌) | `0,4,D,6` (❌) | **0.0%** |
| 542 | Visual Tracking / Recognize numbers and letters | 6,9,8 | `1,2,3` (❌) | `Not enough information` (❌) | `N/A` (❌) | **0.0%** |
| 543 | Visual Tracking / Recognize numbers and letters | 0,9,3 | `N/A` (❌) | `No numbers are present in the image.` (❌) | `Answer` (❌) | **0.0%** |
| 544 | Visual Tracking / Recognize numbers and letters | 3,6,2 | `255,128,0` (❌) | `1,1,1` (❌) | `No numbers present` (❌) | **0.0%** |
| 545 | Visual Tracking / Recognize numbers and letters | 3,7,2 | `3,3,3` (❌) | `N/A` (❌) | `3,3,3` (❌) | **0.0%** |
| 665 | Visual Tracking / Recognize numbers and letters | D, 2, 4 | `N/A` (❌) | `2,0,5` (❌) | `N/A` (❌) | **0.0%** |
| 671 | Visual Tracking / Recognize numbers and letters | C | `C` (✅) | `A` (❌) | `B` (❌) | **33.3%** |
| 757 | Visual Tracking / Recognize numbers and letters | AN APPLE | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 1298 | Visual Tracking / Recognize numbers and letters | J, U, 3 | `W, U, 3` (❌) | `Blue/Teal: W, U; Blue/Cyan: U; Red/Orange: 3` (❌) | `N/A` (❌) | **0.0%** |
| 1587 | Visual Tracking / Recognize numbers and letters | D,8,P,T | `O,S,B,T` (❌) | `D, &, B, X` (❌) | `O,S,P,A` (❌) | **0.0%** |
| 5227 | Visual Tracking / Recognize numbers and letters | 3,4,9 | `N/A` (❌) | `1, 2, 3` (❌) | `1, 3, 9` (❌) | **0.0%** |
| 5228 | Visual Tracking / Recognize numbers and letters | 3,4,5 | `3, 4, 5` (✅) | `2, 3, 4` (❌) | `3,3,4` (❌) | **33.3%** |
| 5229 | Visual Tracking / Recognize numbers and letters | 1,6,7 | `N/A` (❌) | `N/A` (❌) | `1, 6, 9` (❌) | **0.0%** |
| 5238 | Visual Tracking / Recognize numbers and letters | 3,4,9 | `1, 2, 3` (❌) | `None` (❌) | `1, 8, 9` (❌) | **0.0%** |
| 5239 | Visual Tracking / Recognize numbers and letters | 1,4,7 | `No numbers are found` (❌) | `No numbers present` (❌) | `no numbers found` (❌) | **0.0%** |
| 5240 | Visual Tracking / Recognize numbers and letters | 2,5,8 | `1, 6, 8` (❌) | `1, 6, 8` (❌) | `N/A` (❌) | **0.0%** |
| 5241 | Visual Tracking / Recognize numbers and letters | 2,5,9 | `2, 5, 9` (✅) | `2, 5, 9` (✅) | `2,5,9` (✅) | **100.0%** |
| 5242 | Visual Tracking / Recognize numbers and letters | 1,3,7 | `1, 3, 7` (✅) | `3, 3, 7` (❌) | `N/A` (❌) | **33.3%** |
| 5505 | Visual Tracking / Recognize numbers and letters | 2, 7, 5, 9 | `A,S,Z,C` (❌) | `blue,green,red,yellow` (❌) | `A,Z,O,G` (❌) | **0.0%** |
| 5507 | Visual Tracking / Recognize numbers and letters | O, 8, N, Z | `8, Z, N` (❌) | `N/A` (❌) | `8, Z, N` (❌) | **0.0%** |
| 6435 | Visual Tracking / Recognize numbers and letters | 3,6,1 | `N/A` (❌) | `N/A` (❌) | `Not enough information` (❌) | **0.0%** |
| 6509 | Visual Tracking / Recognize numbers and letters | 4, 6, 5, 5 | `N/A` (❌) | `1234` (❌) | `1, 6, 5, 4` (❌) | **0.0%** |
| 8326 | Visual Tracking / Metro map | 6 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8327 | Visual Tracking / Metro map | 8 | `4` (❌) | `N/A` (❌) | `6` (❌) | **0.0%** |
| 8328 | Visual Tracking / Metro map | 11 | `N/A` (❌) | `2` (❌) | `N/A` (❌) | **0.0%** |
| 8329 | Visual Tracking / Metro map | 4 | `5` (❌) | `2` (❌) | `4` (✅) | **33.3%** |
| 8330 | Visual Tracking / Metro map | 8 | `2` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8331 | Visual Tracking / Metro map | 10 | `0` (❌) | `1` (❌) | `1` (❌) | **0.0%** |
| 8332 | Visual Tracking / Metro map | 9 | `0` (❌) | `3` (❌) | `N/A` (❌) | **0.0%** |
| 8339 | Visual Tracking / Metro map | 22 | `N/A` (❌) | `1` (❌) | `1` (❌) | **0.0%** |
| 8340 | Visual Tracking / Metro map | 8 | `N/A` (❌) | `N/A` (❌) | `0` (❌) | **0.0%** |
| 8341 | Visual Tracking / Metro map | 20 | `N/A` (❌) | `3` (❌) | `N/A` (❌) | **0.0%** |
| 8342 | Visual Tracking / Metro map | 12 | `2` (❌) | `N/A` (❌) | `1` (❌) | **0.0%** |
| 8343 | Visual Tracking / Metro map | 11 | `N/A` (❌) | `1` (❌) | `N/A` (❌) | **0.0%** |
| 8162 | Visual Tracking / Lines Observation | 15,13,12,10,9,9,9,8,8,7 | `N/A` (❌) | `N/A` (❌) | `11,10,9,9` (❌) | **0.0%** |
| 8163 | Visual Tracking / Lines Observation | 17,16,12,12,11,11,9,5,4,3 | `N/A` (❌) | `N/A` (❌) | `15,14,12,11,9,8,8` (❌) | **0.0%** |
| 8164 | Visual Tracking / Lines Observation | 14,11,10,9,7,6,4,3 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8165 | Visual Tracking / Lines Observation | 25,7,7,6,6,5,4,4 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8166 | Visual Tracking / Lines Observation | 13,11,10,9,7,6,5,3 | `N/A` (❌) | `N/A` (❌) | `8,8,7,7,5,5,5` (❌) | **0.0%** |
| 8167 | Visual Tracking / Lines Observation | 13,4,17,3,27,14,5,9,8 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8323 | Visual Tracking / Lines Observation | 17,3,6,4,6 | `2,2,2,2,2` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8324 | Visual Tracking / Lines Observation | 13,4,9,15,4,4 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8325 | Visual Tracking / Lines Observation | 14,5,9,4,7,10 | `3,3,4,4,3,3` (❌) | `N/A` (❌) | `3,3,5,5,3,3` (❌) | **0.0%** |
| 431 | Spatial Perception / 3D Views | A | `D` (❌) | `D` (❌) | `D` (❌) | **0.0%** |
| 514 | Spatial Perception / 3D Views | A | `B` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 524 | Spatial Perception / 3D Views | A | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 526 | Spatial Perception / 3D Views | 1-B,2-D,3-A,4-C | `1-A, 2-B, 3-C, 4-D` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | `N/A` (❌) | **0.0%** |
| 527 | Spatial Perception / 3D Views | E | `B` (❌) | `B` (❌) | `C` (❌) | **0.0%** |
| 548 | Spatial Perception / 3D Views | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 562 | Spatial Perception / 3D Views | A | `B` (❌) | `B` (❌) | `C` (❌) | **0.0%** |
| 694 | Spatial Perception / 3D Views | D | `C` (❌) | `C` (❌) | `E` (❌) | **0.0%** |
| 696 | Spatial Perception / 3D Views | D | `C` (❌) | `C` (❌) | `D` (✅) | **33.3%** |
| 713 | Spatial Perception / 3D Views | C | `F` (❌) | `N/A` (❌) | `C` (✅) | **33.3%** |
| 886 | Spatial Perception / 3D Views | C | `A` (❌) | `C` (✅) | `B` (❌) | **33.3%** |
| 888 | Spatial Perception / 3D Views | C | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 2004 | Spatial Perception / 3D Views | A | `B` (❌) | `C` (❌) | `B` (❌) | **0.0%** |
| 4047 | Spatial Perception / 3D Views | A-3,B-1,C-4,D-2,F-5,G-6,E-7,H-8 | `A-3,B-2,C-4,D-2,E-3,F-2,G-7,H-6` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5285 | Spatial Perception / 3D Views | 1-15,2-12,3-14,4-11,5-9,6-16,7-13,8-10 | `1-16, 2-12, 3-15, 4-14, 5-10, 6-9, 7-11, 8-13` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5340 | Spatial Perception / 3D Views | A | `N/A` (❌) | `B` (❌) | `C` (❌) | **0.0%** |
| 5432 | Spatial Perception / 3D Views | C | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 5694 | Spatial Perception / 3D Views | B | `B` (✅) | `B` (✅) | `C` (❌) | **66.7%** |
| 5695 | Spatial Perception / 3D Views | A | `C` (❌) | `B` (❌) | `A` (✅) | **33.3%** |
| 6038 | Spatial Perception / 3D Views | 1-4,2-10,6-8,7-9,11-5,12-3 | `N/A` (❌) | `N/A` (❌) | `1-3,2-4,6-3,7-4,5-5,8-5,10-5,11-3,12-4` (❌) | **0.0%** |
| 6197 | Spatial Perception / 3D Views | 2-8, 1-3, 5-6, 4-7 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6220 | Spatial Perception / 3D Views | 1-12,3-2,5-8,7-4,9-6,11-10 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6280 | Spatial Perception / 3D Views | 1-C, 2-D, 3-A, 4-B. | `N/A` (❌) | `N/A` (❌) | `1-D, 2-B, 3-C, 4-A` (❌) | **0.0%** |
| 6340 | Spatial Perception / 3D Views | 1-8,2-9,3-6,10-4,11-7,12-5 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6378 | Spatial Perception / 3D Views | C | `N/A` (❌) | `N/A` (❌) | `C` (✅) | **33.3%** |
| 6381 | Spatial Perception / 3D Views | 1-2, 4-7,5-10,8-3,9-6 | `N/A` (❌) | `N/A` (❌) | `1-4, 5-8, 9-10` (❌) | **0.0%** |
| 6434 | Spatial Perception / 3D Views | 1-4,3-2,6-5,8-7 | `1-2,3-4,6-5,8-7` (❌) | `1-2,3-4,6-5,8-7` (❌) | `N/A` (❌) | **0.0%** |
| 799 | Spatial Perception / 3D Cube Unfold | 6,7,9 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 1974 | Spatial Perception / 3D Cube Unfold | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 2065 | Spatial Perception / 3D Cube Unfold | The first one in the first row, the third one in the first row | `N/A` (❌) | `N/A` (❌) | `2, 1` (❌) | **0.0%** |
| 3838 | Spatial Perception / 3D Cube Unfold | 3, 5, 6 | `7` (❌) | `7` (❌) | `3, 4, 5, 6` (❌) | **0.0%** |
| 4064 | Spatial Perception / 3D Cube Unfold | E | `C` (❌) | `N/A` (❌) | `B` (❌) | **0.0%** |
| 4077 | Spatial Perception / 3D Cube Unfold | CD | `D` (❌) | `N/A` (❌) | `D` (❌) | **0.0%** |
| 4759 | Spatial Perception / 3D Cube Unfold | B,C | `Answer` (❌) | `N/A` (❌) | `B` (❌) | **0.0%** |
| 4760 | Spatial Perception / 3D Cube Unfold | 2,5 | `3` (❌) | `3` (❌) | `3` (❌) | **0.0%** |
| 5388 | Spatial Perception / 3D Cube Unfold | 2,3,6 | `2, 3, 4, 5, 6, 7` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5449 | Spatial Perception / 3D Cube Unfold | 2,5,7 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6344 | Spatial Perception / 3D Cube Unfold | C | `N/A` (❌) | `C` (✅) | `N/A` (❌) | **33.3%** |
| 6467 | Spatial Perception / 3D Cube Unfold | A | `N/A` (❌) | `D` (❌) | `B` (❌) | **0.0%** |
| 501 | Spatial Perception / Paper Folding | D | `C` (❌) | `D` (✅) | `C` (❌) | **33.3%** |
| 893 | Spatial Perception / Paper Folding | B | `N/A` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 1217 | Spatial Perception / Paper Folding | B | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 3234 | Spatial Perception / Paper Folding | D | `F` (❌) | `C` (❌) | `F` (❌) | **0.0%** |
| 3240 | Spatial Perception / Paper Folding | F | `D` (❌) | `N/A` (❌) | `D` (❌) | **0.0%** |
| 4009 | Spatial Perception / Paper Folding | 1, 2, 3, 1 | `N/A` (❌) | `1,2,4,4` (❌) | `N/A` (❌) | **0.0%** |
| 8333 | Spatial Perception / Paper Folding | 7 | `4` (❌) | `4` (❌) | `3` (❌) | **0.0%** |
| 8334 | Spatial Perception / Paper Folding | 7 | `3` (❌) | `3` (❌) | `3` (❌) | **0.0%** |
| 8335 | Spatial Perception / Paper Folding | 6 | `4` (❌) | `3` (❌) | `5` (❌) | **0.0%** |
| 8336 | Spatial Perception / Paper Folding | 8 | `6` (❌) | `4` (❌) | `3` (❌) | **0.0%** |
| 8337 | Spatial Perception / Paper Folding | 4 | `4` (✅) | `4` (✅) | `8` (❌) | **66.7%** |
| 8338 | Spatial Perception / Paper Folding | 9 | `6` (❌) | `3` (❌) | `5` (❌) | **0.0%** |
| 454 | Spatial Perception / 3D Pattern Completion | A | `C` (❌) | `A` (✅) | `B` (❌) | **33.3%** |
| 480 | Spatial Perception / 3D Pattern Completion | C | `C` (✅) | `C` (✅) | `N/A` (❌) | **66.7%** |
| 481 | Spatial Perception / 3D Pattern Completion | A | `A` (✅) | `B` (❌) | `A` (✅) | **66.7%** |
| 484 | Spatial Perception / 3D Pattern Completion | A | `C` (❌) | `A` (✅) | `A` (✅) | **66.7%** |
| 502 | Spatial Perception / 3D Pattern Completion | B | `B` (✅) | `A` (❌) | `A` (❌) | **33.3%** |
| 505 | Spatial Perception / 3D Pattern Completion | C | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 512 | Spatial Perception / 3D Pattern Completion | A | `N/A` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 621 | Spatial Perception / 3D Pattern Completion | A | `A` (✅) | `A` (✅) | `C` (❌) | **66.7%** |
| 3777 | Spatial Perception / 3D Pattern Completion | A | `C` (❌) | `C` (❌) | `B` (❌) | **0.0%** |
| 4375 | Spatial Perception / 3D Pattern Completion | B | `A` (❌) | `B` (✅) | `A` (❌) | **33.3%** |
| 4391 | Spatial Perception / 3D Pattern Completion | C | `C` (✅) | `C` (✅) | `C` (✅) | **100.0%** |
| 4420 | Spatial Perception / 3D Pattern Completion | A | `B` (❌) | `A` (✅) | `B` (❌) | **33.3%** |
| 4735 | Spatial Perception / 3D Pattern Completion | A | `A` (✅) | `C` (❌) | `A` (✅) | **66.7%** |
| 5308 | Spatial Perception / 3D Pattern Completion | C | `B` (❌) | `C` (✅) | `C` (✅) | **66.7%** |
| 5320 | Spatial Perception / 3D Pattern Completion | A | `B` (❌) | `A` (✅) | `B` (❌) | **33.3%** |
| 5525 | Spatial Perception / 3D Pattern Completion | A | `C` (❌) | `C` (❌) | `B` (❌) | **0.0%** |
| 5531 | Spatial Perception / 3D Pattern Completion | B | `A` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 6430 | Spatial Perception / 3D Pattern Completion | C | `A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 4453 | Spatial Perception / Count 3D blocks | 7 | `9` (❌) | `N/A` (❌) | `7` (✅) | **33.3%** |
| 4456 | Spatial Perception / Count 3D blocks | 7 | `7` (✅) | `5` (❌) | `7` (✅) | **66.7%** |
| 4457 | Spatial Perception / Count 3D blocks | 8 | `6` (❌) | `5` (❌) | `7` (❌) | **0.0%** |
| 4458 | Spatial Perception / Count 3D blocks | 10 | `N/A` (❌) | `11` (❌) | `N/A` (❌) | **0.0%** |
| 4460 | Spatial Perception / Count 3D blocks | 9 | `10` (❌) | `11` (❌) | `11` (❌) | **0.0%** |
| 4593 | Spatial Perception / Count 3D blocks | 9 | `9` (✅) | `10` (❌) | `8` (❌) | **33.3%** |
| 4594 | Spatial Perception / Count 3D blocks | 13 | `10` (❌) | `N/A` (❌) | `15` (❌) | **0.0%** |
| 4596 | Spatial Perception / Count 3D blocks | 13 | `N/A` (❌) | `10` (❌) | `6` (❌) | **0.0%** |
| 4597 | Spatial Perception / Count 3D blocks | 13 | `16` (❌) | `N/A` (❌) | `17` (❌) | **0.0%** |
| 4598 | Spatial Perception / Count 3D blocks | 16 | `8` (❌) | `10` (❌) | `14` (❌) | **0.0%** |
| 4599 | Spatial Perception / Count 3D blocks | 17 | `18` (❌) | `14` (❌) | `N/A` (❌) | **0.0%** |
| 4603 | Spatial Perception / Count 3D blocks | 17 | `N/A` (❌) | `N/A` (❌) | `10` (❌) | **0.0%** |
| 4604 | Spatial Perception / Count 3D blocks | 21 | `10` (❌) | `14` (❌) | `13` (❌) | **0.0%** |
| 4607 | Spatial Perception / Count 3D blocks | 26 | `37` (❌) | `34` (❌) | `38` (❌) | **0.0%** |
| 4610 | Spatial Perception / Count 3D blocks | 13 | `8` (❌) | `14` (❌) | `11` (❌) | **0.0%** |
| 4613 | Spatial Perception / Count 3D blocks | 15 | `10` (❌) | `11` (❌) | `N/A` (❌) | **0.0%** |
| 4614 | Spatial Perception / Count 3D blocks | 18 | `9` (❌) | `14` (❌) | `13` (❌) | **0.0%** |
| 4616 | Spatial Perception / Count 3D blocks | 23 | `27` (❌) | `27` (❌) | `27` (❌) | **0.0%** |
| 4618 | Spatial Perception / Count 3D blocks | 21 | `15` (❌) | `15` (❌) | `16` (❌) | **0.0%** |
| 4619 | Spatial Perception / Count 3D blocks | 21 | `27` (❌) | `19` (❌) | `19` (❌) | **0.0%** |
| 4621 | Spatial Perception / Count 3D blocks | 22 | `20` (❌) | `23` (❌) | `N/A` (❌) | **0.0%** |
| 4624 | Spatial Perception / Count 3D blocks | 19 | `20` (❌) | `14` (❌) | `16` (❌) | **0.0%** |
| 434 | Visual Pattern Recognition / Overlay Patterns | A | `B` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 435 | Visual Pattern Recognition / Overlay Patterns | 2,9 | `9` (❌) | `N/A` (❌) | `1,2,3,4,7,9` (❌) | **0.0%** |
| 438 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `C` (❌) | `B` (❌) | **0.0%** |
| 441 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 458 | Visual Pattern Recognition / Overlay Patterns | A | `N/A` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 465 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 479 | Visual Pattern Recognition / Overlay Patterns | A | `D` (❌) | `D` (❌) | `D` (❌) | **0.0%** |
| 504 | Visual Pattern Recognition / Overlay Patterns | A | `A` (✅) | `C` (❌) | `C` (❌) | **33.3%** |
| 509 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `B` (❌) | `C` (❌) | **0.0%** |
| 536 | Visual Pattern Recognition / Overlay Patterns | 3,9 | `6,7` (❌) | `2,6` (❌) | `1,2` (❌) | **0.0%** |
| 625 | Visual Pattern Recognition / Overlay Patterns | C | `C` (✅) | `C` (✅) | `C` (✅) | **100.0%** |
| 664 | Visual Pattern Recognition / Overlay Patterns | B | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 693 | Visual Pattern Recognition / Overlay Patterns | C | `C` (✅) | `C` (✅) | `C` (✅) | **100.0%** |
| 708 | Visual Pattern Recognition / Overlay Patterns | A | `B` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 3992 | Visual Pattern Recognition / Overlay Patterns | B | `A` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 3993 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 4097 | Visual Pattern Recognition / Overlay Patterns | A | `B` (❌) | `A` (✅) | `B` (❌) | **33.3%** |
| 362 | Visual Pattern Recognition / Logic Patterns | A | `N/A` (❌) | `B` (❌) | `C` (❌) | **0.0%** |
| 448 | Visual Pattern Recognition / Logic Patterns | B | `N/A` (❌) | `D` (❌) | `D` (❌) | **0.0%** |
| 467 | Visual Pattern Recognition / Logic Patterns | F | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 487 | Visual Pattern Recognition / Logic Patterns | A | `B` (❌) | `N/A` (❌) | `B` (❌) | **0.0%** |
| 553 | Visual Pattern Recognition / Logic Patterns | 1 | `N/A` (❌) | `N/A` (❌) | `8` (❌) | **0.0%** |
| 642 | Visual Pattern Recognition / Logic Patterns | C | `N/A` (❌) | `N/A` (❌) | `C` (✅) | **33.3%** |
| 657 | Visual Pattern Recognition / Logic Patterns | F | `3` (❌) | `N/A` (❌) | `C` (❌) | **0.0%** |
| 669 | Visual Pattern Recognition / Logic Patterns | A | `N/A` (❌) | `N/A` (❌) | `A` (✅) | **33.3%** |
| 676 | Visual Pattern Recognition / Logic Patterns | B | `D` (❌) | `C` (❌) | `A` (❌) | **0.0%** |
| 687 | Visual Pattern Recognition / Logic Patterns | E | `N/A` (❌) | `N/A` (❌) | `C` (❌) | **0.0%** |
| 718 | Visual Pattern Recognition / Logic Patterns | E | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 1293 | Visual Pattern Recognition / Logic Patterns | D | `B` (❌) | `A` (❌) | `B` (❌) | **0.0%** |
| 1914 | Visual Pattern Recognition / Logic Patterns | 2-9 | `N/A` (❌) | `N/A` (❌) | `1-7` (❌) | **0.0%** |
| 1925 | Visual Pattern Recognition / Logic Patterns | 3 and 11 | `10 and 11` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 510 | Visual Pattern Recognition / Rotation Patterns | 6,4,2 | `1, 2, 3` (❌) | `4, 5, 6` (❌) | `1,2,3` (❌) | **0.0%** |
| 540 | Visual Pattern Recognition / Rotation Patterns | B | `C` (❌) | `B` (✅) | `A` (❌) | **33.3%** |
| 631 | Visual Pattern Recognition / Rotation Patterns | F | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 684 | Visual Pattern Recognition / Rotation Patterns | C | `C` (✅) | `C` (✅) | `B` (❌) | **66.7%** |
| 4180 | Visual Pattern Recognition / Rotation Patterns | C | `A` (❌) | `A` (❌) | `Choices: (C)` (✅) | **33.3%** |
| 5293 | Visual Pattern Recognition / Rotation Patterns | B | `C` (❌) | `D` (❌) | `C` (❌) | **0.0%** |
| 5519 | Visual Pattern Recognition / Rotation Patterns | C | `C` (✅) | `D` (❌) | `C` (✅) | **66.7%** |
| 5565 | Visual Pattern Recognition / Rotation Patterns | B | `C` (❌) | `D` (❌) | `N/A` (❌) | **0.0%** |
| 6455 | Visual Pattern Recognition / Rotation Patterns | B | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 6462 | Visual Pattern Recognition / Rotation Patterns | B | `B` (✅) | `A` (❌) | `B` (✅) | **66.7%** |
| 537 | Visual Pattern Recognition / Mirroring Patterns | D | `D` (✅) | `C` (❌) | `A` (❌) | **33.3%** |
| 538 | Visual Pattern Recognition / Mirroring Patterns | 1-2,3-6,4-5 | `N/A` (❌) | `1-6, 2-5, 3-4` (❌) | `1-5, 2-4, 3-6` (❌) | **0.0%** |
| 547 | Visual Pattern Recognition / Mirroring Patterns | 8 | `9` (❌) | `9` (❌) | `9` (❌) | **0.0%** |
| 773 | Visual Pattern Recognition / Mirroring Patterns | 1-4,2-5,3-6 | `1-4, 2-5, 3-6` (✅) | `1-6, 2-5, 3-4` (❌) | `1-6, 2-5, 3-4` (❌) | **33.3%** |
| 819 | Visual Pattern Recognition / Mirroring Patterns | C | `D` (❌) | `D` (❌) | `C` (✅) | **33.3%** |
| 1929 | Visual Pattern Recognition / Mirroring Patterns | 1-7, 2-4, 3-10, 5-11, 6-8, 9-12 | `2-3, 6-7, 10-11` (❌) | `3-4, 5-8` (❌) | `N/A` (❌) | **0.0%** |
| 3691 | Visual Pattern Recognition / Mirroring Patterns | C | `C` (✅) | `C` (✅) | `C` (✅) | **100.0%** |
| 4769 | Visual Pattern Recognition / Mirroring Patterns | 1-6, 2-7, 3-4, 5-10, 8-12, 9-11 | `N/A` (❌) | `N/A` (❌) | `1-6,2-5,3-7,4-10,8-11,9-12` (❌) | **0.0%** |
| 4785 | Visual Pattern Recognition / Mirroring Patterns | 1-7, 2-4, 3-5, 6-8 | `N/A` (❌) | `1-8, 2-7` (❌) | `1-8, 2-7, 3-6, 4-5` (❌) | **0.0%** |
| 5288 | Visual Pattern Recognition / Mirroring Patterns | 1-6,2-11,3-9,4-12,5-7,8-10 | `N/A` (❌) | `1-3,4-6,7-9,2-5,10-12,8-11` (❌) | `N/A` (❌) | **0.0%** |
