from matplotlib import pyplot as plt
import numpy as np

class KmerFinder:
    def __init__(self, sequence, k, count_complementary=False):
        self.counts = {}
        for i in range(len(sequence) - k + 1):
            kmer = sequence[i:i + k]
            if count_complementary:
                complementary_kmer = kmer.reverse_complement() # Reverse because the complementary DNA thread is geometrically inverted
                minimum_lex = min(kmer, complementary_kmer) # Count under the same key
                self._add_kmer(minimum_lex)
            else:
                self._add_kmer(kmer)

    def _add_kmer(self, kmer):
        if kmer in self.counts:
            self.counts[kmer] += 1
        else:
            self.counts[kmer] = 1

    def get_max_kmer(self):
        max_kmer = ""
        max_count = 0
        for key, val in self.counts.items():
            if val > max_count:
                max_kmer = key
                max_count = val

        return max_kmer, max_count

    def plot_frequency(self):
        frequency_values = [*self.counts.values()]
        frequency_values.sort()
        plt.plot(np.arange(len(frequency_values)), frequency_values)
        plt.show()

class SkewPlots:
    @staticmethod
    def plot_window_skew(sequence, window_size=1000, dnaA_mid=None):
        cg_skew = []
        at_skew = []

        for i in range(0, len(sequence), window_size):
            chromo_window = sequence[i:i + window_size]
            a_count = chromo_window.count("A")
            t_count = chromo_window.count("T")
            c_count = chromo_window.count("C")
            g_count = chromo_window.count("G")

            cg_skew.append((g_count - c_count) / (g_count + c_count))
            at_skew.append((a_count - t_count) / (a_count + t_count))

        fig, axs = plt.subplots(1, 2, figsize=(12, 4), sharex=True)

        axs[0].plot(at_skew, color="tab:blue")
        axs[0].axhline(0, color="gray", linestyle="--", linewidth=1)
        axs[0].set_title("AT Skew Across Chromosome 1")
        axs[0].set_xlabel(f"Window index ({window_size} bp)")
        axs[0].set_ylabel("AT skew")

        axs[1].plot(cg_skew, color="tab:orange")
        axs[1].axhline(0, color="gray", linestyle="--", linewidth=1)
        axs[1].set_title("CG Skew Across Chromosome 1")
        axs[1].set_xlabel(f"Window index ({window_size} bp)")
        axs[1].set_ylabel("CG skew")

        if dnaA_mid is not None:
            axs[0].axvline(dnaA_mid / window_size, color="red", linestyle="--", linewidth=1.5, label="DnaA midpoint")
            axs[1].axvline(dnaA_mid / window_size, color="red", linestyle="--", linewidth=1.5, label="DnaA midpoint")

        fig.tight_layout()
        plt.show()

    @staticmethod
    def plot_diagram_skew(sequence, dnaA_mid=None):
        seq = np.frombuffer(str(sequence).encode(), dtype='S1')

        is_G = (seq == b'G')
        is_C = (seq == b'C')
        is_A = (seq == b'A')
        is_T = (seq == b'T')

        cg = is_G.astype(int) - is_C.astype(int)
        at = is_A.astype(int) - is_T.astype(int)

        cg_skew = np.cumsum(cg)
        at_skew = np.cumsum(at)

        min_cg_skew = np.argmin(cg_skew)

        plt.plot(cg_skew, label="GC skew")
        plt.plot(at_skew, label="AT skew")
        plt.axvline(min_cg_skew, linestyle="--", label="min CG skew")
        if dnaA_mid is not None:
            plt.axvline(dnaA_mid, linestyle="--", label="dnaA")

        plt.legend(loc="center")
        plt.show()

        return min_cg_skew